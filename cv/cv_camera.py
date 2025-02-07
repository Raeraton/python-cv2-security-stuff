import cv.frame_mod_lib as frame_mod_lib
import cv.logger as logger
import cv.video_capture as video_capture

import cv2
from time import time






def run_camera( capture_target, fd_action, fd_rest, action_wait_time ):

	log = logger.My_logger()

	video = cv2.VideoCapture(capture_target)
	if (video.isOpened() == False):
		print("Error reading video file")

	frame_size = ( int(video.get(3)), int(video.get(4)) )


	video_saver = video_capture.Video_capturer( frame_size=frame_size, spf=fd_action )




	check, frame = video.read()
	static_back = frame_mod_lib.get_static_reference( frame=frame )



	timereference = time()
	timepoint = 0
	inmotion = False
	mode = ''
	motion_start_time = 0
	delay = fd_action
	while True:
		frame_time = time()
		_, frame = video.read()


		if (frame_time-timereference) * 1000 > delay:

			frame, tre, gray, motion = frame_mod_lib.create_frames( frame=frame, reference_frame=static_back )

			if motion:
				delay = fd_action
				timepoint = frame_time
				if not inmotion:
					motion_start_time = frame_time
					inmotion = True
					mode = "Action"
			elif frame_time - timepoint > action_wait_time:
				if motion_start_time != -1:
					log.add_log( f"{frame_time-motion_start_time}" )
					motion_start_time = -1
				delay = fd_rest
				inmotion = False
				mode = "Rest"



			frame_mod_lib.addinfo2frame( frame, frame_time, mode )



			video_saver.add_frame( frame )
			static_back = gray


			
			cv2.imshow("rect Frame", frame)
			cv2.imshow("tre Frame", tre)

			timereference = frame_time


		key = cv2.waitKey(1) 
		if key == ord('q'):
			break






	log.close()
	video_saver.release()


	video.release() 
	cv2.destroyAllWindows() 
