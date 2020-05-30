import configparser
import os
import numpy as np

# from multiprocessing import Process, Queue 
from config import CONFIG_PATH

import pyrealsense2 as rs
import logging

logger = logging.getLogger('Camera')

class Camera:

    class cmd:
        READY = 'READY'
        QUIT = 'QUIT'
        GETFRAME = 'GETFRAME'

    def __init__(self):
        self.width = 640
        self.height = 480
        self.frame = 30
        self.camera_type = 'rs2'
        # self.run = self.run_rs2
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read(CONFIG_PATH)
        if cfg_parser.has_section('Camera'):
            self.camera_type = cfg_parser.get('Camera', 'type')
            for option in cfg_parser.options('Camera'):
                if option == 'type': continue
                self.__dict__[option] = cfg_parser.get('Camera', option)
        # self.q = Queue()
        if self.camera_type == 'rs2':
            self.init_device = self.init_device_rs2
        self.init_device()
        self.is_running = False
        self.camera_status = False
        # self.worker = Process(target=self.run, args=(self.q,))

    def init_device_rs2(self):
        try:
            self.pipeline = rs.pipeline()
            self.config = rs.config()
            self.config.enable_stream(
                rs.stream.depth, self.width, self.height,
                rs.format.z16, self.frame)
            self.profile = self.pipeline.start(self.config)
            self.depth_sensor = self.profile.get_device().first_depth_sensor()

            preset_range = self.depth_sensor.get_option_range(rs.option.visual_preset)
            print(str(preset_range))
            for i in range(int(preset_range.max)):
                visulpreset = self.depth_sensor.get_option_value_description(
                    rs.option.visual_preset,i)
                print('%02d: %s' % (i, visulpreset))
                if visulpreset == 'Hand':
                    self.depth_sensor.set_option(rs.option.visual_preset, i)
            self.depth_scale = self.depth_sensor.get_depth_scale()
            self.camera_status = True
        except Exception as e:
            logger.error(e)
            self.camera_status = False
            print(self.camera_status)
            raise

    def get_frame(self):
        try:
            frames = self.pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            depth_image = np.asarray(depth_frame.get_data(), dtype=np.float32)
            depth = depth_image * self.depth_scale * 1000
            depth[depth == 0] = depth.max()
            return depth
        except Exception as e:
            logger.error(e)
            raise

    def stop(self):
        self.pipeline.stop()

    def get_status(self):
        return self.camera_status

    # def start(self):
    #     self.pipeline.start()

    """
    def start(self):
        self.worker.start()
        self.is_running = True
        if (self.q.get() != self.cmd.READY):
            self.is_running = False
            self.worker.terminate()
            return -1
        return 0

    def get_frame(self):
        try:
            self.q.put(self.cmd.GETFRAME)
            return self.q.get(False)
        except Exception:
            return None

    def quit(self):
        self.is_running = False
        self.q.put(self.cmd.QUIT)

    def run_rs2(self, q):
        # running = True
        pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(
            rs.stream.depth, self.width, self.height,
            rs.format.z16, self.frame)
        profile = pipeline.start(config)
        depth_sensor = profile.get_device().first_depth_sensor()

        preset_range = depth_sensor.get_option_range(rs.option.visual_preset)
        print(str(preset_range))
        for i in range(int(preset_range.max)):
            visulpreset = depth_sensor.get_option_value_description(
                rs.option.visual_preset,i)
            print('%02d: %s' % (i, visulpreset))
            if visulpreset == 'Hand':
                depth_sensor.set_option(rs.option.visual_preset, i)
        depth_scale = depth_sensor.get_depth_scale()
        q.put(self.cmd.READY)

        while True:
            cmd = q.get()
            if cmd == self.cmd.GETFRAME:
                frames = pipeline.wait_for_frames()
                depth_frame = frames.get_depth_frame()
                depth_image = np.asarray(depth_frame.get_data(), dtype=np.float32)
                depth = depth_image * depth_scale * 1000
                depth[depth == 0] = depth.max()
                q.put(depth)
            elif cmd == self.cmd.QUIT:
                break

        pipeline.stop()
"""
