import cv.cv_camera as camera
import server.server as server


import _thread


_thread.start_new_thread( camera.run_camera, ( "http://192.168.1.24:8080/video", 25, 1000, 3 ) )
_thread.start_new_thread( server.start_server, () )



while input() != 'shutdown':
    pass