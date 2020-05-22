# this file makes the .dat file from the original video
# the .dat file has the frames ready to play using main.py

import os,sys
import numpy as np
import cv2

video = cv2.VideoCapture('matrix2.mp4')
vfc = -1 # start naming at 0

if not os.path.isdir('frames'):
    os.makedirs('frames')

openfile = open('the_matrix.dat',mode='wb') 

##cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
##cv2.createTrackbar('value1','frame',3,25,lambda x:x)
##cv2.createTrackbar('value2','frame',1,25,lambda x:x)


while 1:

    try:

        retv,frame = video.read()

        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # image needs to be cropped from 1280x720 to 1280x532 = widescreen 2.39
        #frame = frame[94:94+532, 0:1280]

        # oled is 128x64 = 2.0
        # crop from 1280 to 1064
        #frame = frame[0:532, 108:108+1064]

        # combined crop to 1064x532
        frame = frame[94:94+532, 108:108+1064]

        # resize
        frame = cv2.resize(frame,(128,64),interpolation=cv2.INTER_LINEAR)

    ##    # get values
    ##    value1 = cv2.getTrackbarPos('value1','frame')
    ##    value2 = cv2.getTrackbarPos('value2','frame')
    ##    if value1%2==0:
    ##        value1 += 1
    ##    if value2%2==0:
    ##        value2 += 1

        retv,frame = cv2.threshold(frame,40,255,cv2.THRESH_BINARY)
        #retv,frame = cv2.threshold(frame,32,255,cv2.THRESH_BINARY_INV)
        #frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,value1,value2)
        #frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,value1,value2)

        #frame = cv2.Canny(frame,value1,value2)

        # check for blank frames
        if 1: #np.sum(frame):

            vfc += 1
            if vfc >= 100 and vfc%100==0:
                print(vfc)

            # write frame to file
            # this is the format used by the oled
            ba = bytearray()
            for page in range(8):
                for col in range(128):
                    byte = 0
                    orv = 1
                    for y in range(8):
                        row = page*8 + y
                        if frame[row][col]:
                            byte |= orv
                        orv *= 2                
                    ba.append(byte)
            openfile.write(bytes(ba))

            # show
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # done
        if 0:#vfc >= 6112:
            break

    except:
        break

openfile.close() 

video.release()
cv2.destroyAllWindows()

print(vfc,'frames')
