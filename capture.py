import time
import picamera
import sys

if len(sys.argv) == 1:
    name = 'image.data'
else:
    name = 'image' + sys.argv[1] + '.data'

    
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 80
    time.sleep(2)
    camera.shutter_speed=300
    camera.exposure_mode = 'off'

#    camera.start_preview()
#    time.sleep(2)
    camera.capture(name, 'rgb')
#    time.sleep(t)
#    camera.stop_preview()
