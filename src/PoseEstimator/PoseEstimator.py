# from estimator.estimator import Estimator
from multiprocessing import Process, Queue
# from Camera import camera


class CMD:
    READY = 'READY'
    QUIT = 'QUIT'
    GETPOSE = 'GETPOSE'

class PoseEstimator:

    def __init__(self):
        self.q = Queue()
        # self.e = Estimator()
        self.is_running = False
        self.worker = Process(target=run, args=(self.q,))

    def start(self):
        self.worker.start()
        self.is_running = True
        if self.q.get() != CMD.READY:
            self.is_running = False
            self.worker.terminate()
            return -1
        return 0

    def stop(self):
        self.q.put(CMD.QUIT)
        self.worker.terminate()
    
    def get_pose(self):
        self.q.put(CMD.GETPOSE)
        res = self.q.get()
        # print(res)
        results, img_show = res['results'], res['img_show']
        return results, img_show


def run(q: Queue):
    from Camera.Camera import Camera
    from estimator.estimator import Estimator
    camera = Camera()
    estimator = Estimator()
    q.put(CMD.READY)
    while True:
        frame = camera.get_frame()
        r, i = estimator.get_result(frame)
        cmd = q.get()
        if cmd == CMD.GETPOSE:
            q.put({'results': r, 'img_show': i})
        elif cmd == CMD.QUIT:
            break
    camera.stop()
