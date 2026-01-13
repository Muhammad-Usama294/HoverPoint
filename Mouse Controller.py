import cv2
import time
import numpy as np
import HandTrackingModule as htm
#import autopy

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
while True:
    # find hand landmarks
    success, img = cap.read
    img = detector.findHands(img)
    lmList, bbox = detector.findPositions(img, draw=False)

    # get the tip of index and middle
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    # check the up fingers
    # only index finger.. move mouse
    #convert coordinates
    # move mouse
    # both fingers.. click mode
    # find distance between both
    # click if short

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)