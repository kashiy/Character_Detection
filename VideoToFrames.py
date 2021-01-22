import cv2
import numpy as np
import os
import glob

def video_to_frames():
    # Playing video from file:
    cap = cv2.VideoCapture(r"C:\Users\Yuval Kashi\Downloads\rick_video.mp4")

    filename = 'data_video_to_frames'
    try:
        if not os.path.exists(filename):
            os.makedirs(filename)
        else:
            files = glob.glob(os.getcwd() + "\\" + filename + "\\*")
            for f in files:
                os.remove(f)
    except OSError:
        print('Error: Creating directory of ' + filename)

    currentFrame = 0
    i=100
    while(i>0):
        # Capture frame-by-frame

        ret, frame = cap.read()

        #PRINTS 1 FRAME EVERY 100 FRAMES
        if currentFrame%50 == 0:
            # Saves image of the current frame in jpg file
            name = './'+filename+'/frame' + str(currentFrame) + '.jpeg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1
        i = i - 1
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return os.getcwd()+"\\"+filename

# print(video_to_frames())
