import time
import picamera

#import sys

#if len(sys.argv) == 1:
#    t = 5
#else:
#    t = float(sys.argv[1])

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 80
    time.sleep(2)
    camera.shutter_speed=200
    camera.exposure_mode = 'off'

    camera.start_preview()
    time.sleep(20000)
#    camera.capture('image.data', 'rgb')
#    time.sleep(t)
#    camera.stop_preview()
