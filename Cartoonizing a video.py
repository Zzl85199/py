#pip uninstall opencv-python
#pip install opencv-python
#pip install opencv-python-headless
#pip install opencv-contrib-python

"""Accessing the Webcam"""
#import cv2
#import numpy as np
#from enum import Enum
#
## Default webcam: 0 => face back
##         webcam: 1 => face forward
#BACKWARD = 0
#FORWARD = 1
#
#face_direction = BACKWARD
#cap = cv2.VideoCapture(face_direction)
#
## Check if the webcam is opened correctly
#if not cap.isOpened():
#    raise IOError("Cannot open webcam")
#
#while True:
#    ret, frame = cap.read()
#    shape = frame.shape
#    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#    frame[:,:,:] = frame[:,::-1,:] if face_direction==BACKWARD else frame[:,:,:]
#    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
#    #frame[:,:,0] = cv2.equalizeHist(frame[:,:,0])
#    #frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR)
#    cv2.imshow("Captured video", frame)
#     
#    c = cv2.waitKey(1)   # take the ASCII code of the keystroke
#    if c==27 or c==ord('c') or c==ord('C'):
#        break
#    
#cap.release()
#cv2.destroyAllWindows()
#cv2.waitKey(1)

"""Keyboard Inputs"""
#import cv2
#
#def print_howto():
#    print("""
#         Change color space of the
#         input video stream using keyboard controls. The control keys are:
#         1. Grayscale - press 'g'
#         2. YUV - press 'y'
#         3. HSV - press 'h'
#         4. Quit - press ESC button
#         5. Normal color mode - press other keys
#         """)
#    
#if __name__=='__main__':
#    
#    print_howto()
#    cap = cv2.VideoCapture(0)
#    
#    # Check if the webcam is opened correctly
#    if not cap.isOpened():
#           raise IOError("Cannot open webcam")
#    cur_mode = None
#    
#    while True:
#        
#        # Read the current frame from webcam
#        ret, frame = cap.read()
#        
#        # Resize the captured image
#        frame = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
#        
#        c = cv2.waitKey(1)  # c is the ASCII code of the keystroke
#        if c == 27:
#            break
#            
#        # Update cur_mode only in case it is different and key was pressed
#        # In case a key was not pressed during the iteration result is -1
#        # or 255, depending on library versions
#        if c != -1 and c != 255 and c != cur_mode:
#            cur_mode = c
#        
#        if cur_mode == ord('g'):
#            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#        elif cur_mode == ord('y'):
#            output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
#        elif cur_mode == ord('h'):
#            output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#        else:
#            output = frame
#        
#        cv2.imshow('Webcam', output[:,::-1])
#        
#    cap.release()
#    cv2.destroyAllWindows()
#    cv2.waitKey(1)


"""Mouse Inputs"""
#import cv2
#import numpy as np
#
#def detect_quadrant(event, x, y, flags, param):
#    
#    # Retrieve the imaeg reference and its shape
#    img = param["board"]
#    height,width = img.shape[:2]
#    
#    if event == cv2.EVENT_LBUTTONDOWN:
#        if x > width/2:
#            if y > height/2:
#                point_top_left = (int(width/2), int(height/2))
#                point_bottom_right = (width-1, height-1)
#            else:
#                point_top_left = (int(width/2), 0)
#                point_bottom_right = (width-1, int(height/2))
#        else:
#            if y > height/2:
#                point_top_left = (0, int(height/2))
#                point_bottom_right = (int(width/2), height-1)
#            else:
#                point_top_left = (0, 0)
#                point_bottom_right = (int(width/2), int(height/2))
#              
#        # Paint all in white and paint specified quadrant with green 
#        cv2.rectangle(img, (0,0), (width-1,height-1), (255,255,255), -1)
#        cv2.rectangle(img, point_top_left, point_bottom_right, (200,0,0), -1)
#        
#if __name__=='__main__':
#    
#    #width, height = 640, 480
#    nRow,nCol = 480, 640
#    img = 255 * np.ones((nRow, nCol, 3), dtype=np.uint8)
#    
#    cv2.namedWindow('Click Board')
#    cv2.setMouseCallback('Click Board', detect_quadrant, {"board": img})
#    
#    while True:
#        cv2.imshow('Click Board', img)
#        c = cv2.waitKey(1)
#        if c == 27:
#            break
#    
#    cv2.destroyAllWindows()
#    cv2.waitKey(1)


"""Negative Filming a Live Video"""
#import cv2
#import numpy as np
#
#"""*******************************************************************************
#Function: update_pts()
#Description: Update the bounding box's four corners.
#*******************************************************************************"""
#def update_pts(params, x, y):
#    global x_init, y_init
#    params["top_left_pt"] = (min(x_init, x), min(y_init, y))
#    params["bottom_right_pt"] = (max(x_init, x), max(y_init, y))
#    
#    # perform the negative filming effect
#    #img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
#    
#"""*******************************************************************************
#Function: draw_rectangel()
#Description: Define the coordinates of the bounding box's four corners. No actual
#  drawing is performed here
#*******************************************************************************"""
#def draw_rectangle(event, x, y, flags, params):
#    global x_init, y_init  # drawing
#    
#    # First click initialize the init rectangle point
#    if event == cv2.EVENT_LBUTTONDOWN:
#        x_init, y_init = x, y
#        
#    # Meanwhile mouse button is pressed, update diagonal rectangle point
#    # flag&cv2.EVENT_FLAG_LBUTTON detects whether left button is pressed when moving
#    elif event == cv2.EVENT_MOUSEMOVE and (flags&cv2.EVENT_FLAG_LBUTTON):
#        update_pts(params, x, y)
#        
#    # Once mouse botton is release
#    # update_pts() determines the bounding box 
#    elif event == cv2.EVENT_LBUTTONUP:
#        update_pts(params, x, y)
#
#"""*************************
#MAIN program starts here.
#*************************"""
#if __name__=='__main__':
#    
#    x_init = -1
#    y_init = -1
#    
#    # drawing = False
#    event_params = {"top_left_pt": (-1, -1), "bottom_right_pt": (-1, -1)}
#    cap = cv2.VideoCapture(0)
#    
#    # Check if the webcam is opened correctly
#    if not cap.isOpened():
#        raise IOError("Cannot open webcam")
#
#    window_title = "Negative Filming a Live Video"
#    cv2.namedWindow(window_title)
#    # Bind draw_rectangle function to every mouse event
#    cv2.setMouseCallback(window_title, draw_rectangle, event_params)
#    
#    while True:
#        ret, frame = cap.read()
#        frame[:,:,:] = frame[:,::-1,:]
#        img = cv2.resize(frame, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_AREA)
#        (x0,y0), (x1,y1) = event_params["top_left_pt"], event_params["bottom_right_pt"]
#        img[y0:y1, x0:x1] = 255 - img[y0:y1, x0:x1]
#        cv2.imshow(window_title, img)
#        c = cv2.waitKey(1)
#        if c == 27:
#            break
#    cap.release()
#    cv2.destroyAllWindows()
#    cv2.waitKey(1)


"""Cartoonizing an Image"""
#import cv2
#import numpy as np
#
#def print_howto():
#    print("""
#    Change cartoonizing mode of image:
#    1. Cartoonize without Color - press 's'
#    2. Cartoonize with Color - press 'c'
#    """)
#    
#"""***************************************************************************
#Function: cartoonize_image
#Description: Create cartoon effect => objects blurred w/wo sketched outlines
#  (1) To determine the sketches outlines, the image is gray-scaled and the
#      objects' contours are high-lighted by using the Laplacian operator. An
#      inverse thresholding is then performed to label the contours as "black"
#      and the background as "white." 
#  (2) The thresholded output is the outline-only cartoon image.
#  (3) To create a blurred image with outlines, the previously thresholded 
#      output serves as a mask.
#  (4) The original image is blurred by cv2.bilateralFilter() many times. The 
#      image is scaled down to gain filtering performance. The filtered output
#      is then scaled up back to its original size.
#  (5) The filtered image overlayed with the sketched outlines creates the 
#      blurred image with outlines. 
#***************************************************************************"""
#def cartoonize_image(img, ksize=5, sketch_mode=False):
#    
#    # ksize: kernel size for Laplacian filtering and bilateral filtering
#    # sketch_mode: True for outline, False for additional objects themselves
#    
#    # Constants used for bilateral filtering cv2.bilateralFilter()
#    # nRepetition: number of repititions to blur the image
#    # sigmaR: sigma in range (color difference)
#    # sigmaS: sigma in space (coordinate distance)
#    nRepetition = 10
#    sigmaR,sigmaS = 5,7
#    
#    # Create the sketch
#    # (1) Convert the image to gray-scaled
#    # (2) Apply Laplacian of Gaussian/median blur to high-light the contour
#    # (3) Apply (inverse-)thresholding to create a mask
#    
#    # Blur kernel (nKernel) and Gaussian kernel (gKernel)
#    nKernel = 7
#    gKernel = (nKernel,nKernel)
#    sigmaX = 0
#    
#    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    edges = cv2.Laplacian(cv2.GaussianBlur(img_gray,gKernel,sigmaX),cv2.CV_8U,ksize=ksize)
#    #edges = cv2.Laplacian(img_gray,cv2.CV_8U,ksize=ksize)
#    #edges = cv2.Laplacian(cv2.medianBlur(img_gray, nKernel), cv2.CV_8U, ksize=ksize)
#    __, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
#    
#    # Thicken the contour lines by using cv2.erode()
#    # Currently, the contour is represented by low-intensity (black) pixels. Eroding white 
#    # pixels is de facto thickening the black lines.
#    morphology_kernel = np.ones((3,3), np.uint8)
#    mask = cv2.erode(mask, morphology_kernel, iterations=1)
#      
#    # 'mask' is the sketch of the image
#    if sketch_mode:
#        return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
#    
#    # To create the blurred image
#    # (1) Down scale the image
#    # (2) Apply bilateral filtering for several times
#    # (3) Restore the image to its original size
#    
#    # Down-scaling the image to expedite the filtering process
#    nScaling = 0.25
#    
#    img_small = cv2.resize(img,None,fx=nScaling,fy=nScaling,interpolation=cv2.INTER_AREA)
#    for i in range(nRepetition):
#        img_small = cv2.bilateralFilter(img_small, ksize, sigmaR, sigmaS)
#        #img_small = cv2.Laplacian(img_small, cv2.CV_8U, ksize=ksize)
#    img_output = cv2.resize(img_small, None, fx=1.0/nScaling, fy=1.0/nScaling,
#                            interpolation=cv2.INTER_LINEAR)
#    
#    # Add the thick boundary lines to the image using 'AND' operator
#    # Actually, the thick boundary lines were masked out!!
#    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
#    
#    return dst
#
#if __name__=='__main__':
#    
#    print_howto()
#    
#    cap = cv2.VideoCapture(0)
#
#    cur_mode = None
# 
#    while True:
#               
#        __, frame = cap.read()
#        frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
#        
#        c = cv2.waitKey(1)
#        if c == 27:
#            break
#        
#        #cur_mode = c if (c != -1 and c != 255 and c != cur_mode) else cur_mode
#        cur_mode = c if (c not in [-1,255,cur_mode]) else cur_mode
#
#        if cur_mode in [ord('s'),ord('S')]:
#            cv2.imshow('Cartoonize',cartoonize_image(frame,ksize=5,sketch_mode=True)[:,::-1])
#        elif cur_mode in [ord('c'),ord('C')]:
#            cv2.imshow('Cartoonize',cartoonize_image(frame,ksize=5,sketch_mode=False)[:,::-1])
#        else:
#            cv2.imshow('Cartoonize', frame[:,::-1])
#            
#    cap.release()
#    cv2.destroyAllWindows()
#    cv2.waitKey(1)


"""Exercise"""
import cv2
import numpy as np

def print_howto():
    print("""
    Change cartoonizing mode of image:
    1. Cartoonize without Color - press 's'
    2. Cartoonize with Color - press 'c'
    """)
    
"""***************************************************************************
Function: cartoonize_image
Description: Create cartoon effect => objects blurred w/wo sketched outlines
  (1) To determine the sketches outlines, the image is gray-scaled and the
      objects' contours are high-lighted by using the Laplacian operator. An
      inverse thresholding is then performed to label the contours as "black"
      and the background as "white." 
  (2) The thresholded output is the outline-only cartoon image.
  (3) To create a blurred image with outlines, the previously thresholded 
      output serves as a mask.
  (4) The original image is blurred by cv2.bilateralFilter() many times. The 
      image is scaled down to gain filtering performance. The filtered output
      is then scaled up back to its original size.
  (5) The filtered image overlayed with the sketched outlines creates the 
      blurred image with outlines. 
      
***************************************************************************"""
def cartoonize_image(img, ksize=5, sketch_mode=False):
    
    # ksize: kernel size for Laplacian filtering and bilateral filtering
    # sketch_mode: True for outline, False for additional objects themselves
    
    # Constants used for bilateral filtering cv2.bilateralFilter()
    # nRepetition: number of repititions to blur the image
    # sigmaR: sigma in range (color difference)
    # sigmaS: sigma in space (coordinate distance)
    nRepetition = 10
    sigmaR,sigmaS = 7,11
    
    # Create the sketch
    # (1) Conver the image to gray-scaled
    # (2) Apply Laplacian of Gaussian/median blur to high-light the contour
    # (3) Apply (inverse-)thresholding to create a mask
    
    # Blur kernel (nKernel) and Gaussian kernel (gKernel)
    nKernel = 7
    gKernel = (nKernel,nKernel)
    sigmaX = 0
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian(cv2.GaussianBlur(img_gray,gKernel,sigmaX),cv2.CV_8U,ksize=ksize)
    #edges = cv2.Laplacian(cv2.medianBlur(img_gray, nKernel), cv2.CV_8U, ksize=ksize)
    __, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    
    # Thicken the contour lines by using cv2.erode()
    # Currently, the contour is represented by low-intensity (black) pixels. Eroding white 
    # pixels is de facto thickening the black lines.
    morphology_kernel = np.ones((3,3), np.uint8)
    mask = cv2.erode(mask, morphology_kernel, iterations=1)
      
    # 'mask' is the sketch of the image
    if sketch_mode:
        return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # To create the blurred image
    # (1) Down scale the image
    # (2) Apply bilateral filtering for several times
    # (3) Restore the image to its original size
    
    # Down-scaling the image to expedite the filtering process
    nScaling = 1 # 0.25
    
    img_small = cv2.resize(img,None,fx=nScaling,fy=nScaling,interpolation=cv2.INTER_AREA)
    for i in range(nRepetition):
        img_small = cv2.bilateralFilter(img_small, ksize, sigmaR, sigmaS)
    img_output = cv2.resize(img_small, None, fx=1.0/nScaling, fy=1.0/nScaling,
                            interpolation=cv2.INTER_LINEAR)
    
    # Add the thick boundary lines to the image using 'AND' operator
    # Actually, the thick boundary lines were masked out!!
    #dst = img_output
    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
    
    return dst


if __name__=='__main__':
    
    print_howto()
    
    cap = cv2.VideoCapture('20241204testingvideo.wmv')
    if (not cap.isOpened()):
        print("Error opening video stream or file")
        #cap.release()
        #return
    
    # Default resolutions of the frame are obtained.The default resolutions 
    # are system dependent.We convert the resolutions from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    
    # Define the codec and create VideoWriter object.
    cap_out = cv2.VideoWriter('20241204testingvideo_cartoon.avi',
                              cv2.VideoWriter_fourcc('M','J','P','G'), 
                              30,    # frame rate fps 
                              (frame_width,frame_height))
    
    cur_mode = None
 
    while cap.isOpened():
               
        success, frame = cap.read()
        
        if not success:
            break
            
        #frame = cv2.resize(frame, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
        
        c = cv2.waitKey(5)
        if c == 27:
            break
        
        cur_mode = c if (c != -1 and c != 255 and c != cur_mode) else cur_mode

        if cur_mode == ord('s'):
            frame_cartoon = cartoonize_image(frame,ksize=5,sketch_mode=True)
            cv2.imshow('Cartoonize',frame_cartoon)
        elif cur_mode == ord('c'):
            frame_cartoon = cartoonize_image(frame,ksize=5,sketch_mode=False)
            cv2.imshow('Cartoonize',frame_cartoon)
        else:
            frame_cartoon = frame
            cv2.imshow('Cartoonize', frame)
            
        cap_out.write(frame_cartoon)
            
    cap.release()
    cap_out.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

 #錄影連結:https://changgunguniversity-my.sharepoint.com/:v:/g/personal/m1344009_cgu_edu_tw/Ef_V1sAfUWRImIA8HX1ya8kB9qn9SrSazvggAiVu_PrwBg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=zdrPo0