import cv2

from datetime import datetime


MAX_FRAME_PER_VIDEO = 3600




class Video_capturer:

    vc: cv2.VideoWriter
    frame_count:int
    frame_size: tuple[int, int]
    spf:float


    def __init__(self, frame_size, spf):
        self.frame_size = frame_size
        self.spf = spf

        self.open_file()




    def open_file(self):
        self.vc = cv2.VideoWriter(	f"recs/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.avi",
										cv2.VideoWriter_fourcc(*'XVID'),
										1000/self.spf,
										self.frame_size )
        
        self.frame_count = 0
    


    def add_frame( self, frame ):
        self.vc.write( frame )
        self.frame_count += 1

        if self.frame_count == MAX_FRAME_PER_VIDEO:
            self.release()
            self.open_file()



    
    def release(self):
        self.vc.release()



