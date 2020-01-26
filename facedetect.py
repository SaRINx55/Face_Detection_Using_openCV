# import required packages
import cv2
import dlib
import time
import os
#Enter Video Diretory name
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
videofiles=input("Enter the folder name where all videos are saved:-")
VID_DIR=os.path.join(BASE_DIR,videofiles)
frames=input("Enter the folder name to save the frames:-")
FRAME_DIR=os.path.join(BASE_DIR,frames)
for dirpath, dnames, fnames in os.walk(VID_DIR):
    i=1
    for f in fnames:
        if f.endswith(".mp4") or f.endswith(".avi"):
            frame_folder_name="videofile"+str(i)
            print(VID_DIR +"/"+f)
            os.chdir(FRAME_DIR)
            os.mkdir(frame_folder_name)
            NEW_DIR=os.path.join(FRAME_DIR,frame_folder_name)
            os.chdir(NEW_DIR)
            vidcap = cv2.VideoCapture(VID_DIR +"/"+f)

            #Convert video to frames
            success,image = vidcap.read()

            if image is None:
                print("Could not read input image")
                exit()

            # initialize hog + svm based face detector
            hog_face_detector = dlib.get_frontal_face_detector()


            j=0
            while success:
                start = time.time()

                # apply face detection (hog)
                faces_hog = hog_face_detector(image, 1)

                end = time.time()
                print("Execution Time (in seconds) :")
                print("HOG : ", format(end - start, '.2f'))
                # loop over detected faces

                for face in faces_hog:
                    x = face.left()
                    y = face.top()
                    w = face.right() - x
                    h = face.bottom() - y
                    faceimg = image[y:y+h,x:x+w]
                    j += 1
                cv2.imwrite("frame%d.png" %j, faceimg)



                img_height, img_width = image.shape[:2]
                # save output image
                success,image = vidcap.read()
        i = i+1


        os.chdir(BASE_DIR)
        print(os.getcwd())
