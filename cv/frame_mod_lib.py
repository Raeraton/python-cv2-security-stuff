import cv2

from time import ctime


def get_static_reference( frame ):
    gray = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    return gray





#mystatic lib
def draw_bigest_contour_and_test_movement( cnts, frame ) -> bool:
    bigest_contour = None
    max_area = 0

    for contour in cnts:
        carea = cv2.contourArea(contour)
        if carea > max_area  and  carea > 64:
            max_area = carea
            bigest_contour = contour

    x, y, w, h = cv2.boundingRect(bigest_contour)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    if max_area == 0:
        return False
    return True







def create_frames( frame, reference_frame ):
    gray = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
    gray = cv2.GaussianBlur(gray, (21, 21), 0)


    thresh_frame = cv2.absdiff( reference_frame, gray )
    thresh_frame = cv2.threshold(thresh_frame, 10, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)


    cnts, _ = cv2.findContours( thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )


    rect_frame = frame.copy()
    motion = draw_bigest_contour_and_test_movement( cnts, rect_frame )    
    


    return [ rect_frame, thresh_frame, gray, motion ]




def addinfo2frame( frame, time, addinf ):
    return cv2.putText( frame, f"{ctime(time)} {addinf}", (70,30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0) )