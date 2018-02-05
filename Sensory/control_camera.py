from flask import Flask, render_template, Response
from imutils.video.pivideostream import PiVideoStream
import time 
import numpy as np
import cv2

class VideoCamera(object):
    def __init__(self, flip=False):
        self.vs = PiVideoStream().start()
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
        


video_camera = VideoCamera(flip=False)
app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' 
                +frame+ b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera), 
            mimetype='multipart/x-mixed-replace; boundary=frame')

def camera():
    print("welcome to 192.168.0.220:5000/video_feed")
    app.run(host='0.0.0.0', debug=False)


if __name__ == '__main__':
    camera()
