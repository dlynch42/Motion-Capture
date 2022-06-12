import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture('/Users/devinlynch/MoCap2/Video.mov')

detector = PoseDetector()   # no parameters needed in this case
posList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)    # Get pose
    lmList, bboxInfo = detector.findPosition(img)  # Landmark List and BoundingBox info from pose

    if bboxInfo:
        lmString = ''   # will have all points in it; keep empty
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0]-lm[2]},{lm[3]},'    # img.shape[0] = height; need comma at the end so that there the array looks better
        posList.append(lmString)

    print(len(posList))     # number of frames

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)  # 1 millisecond delay
    if key == ord('s'):     # export to text file
        with open("AnimationFile.txt", 'w') as f:   # w = writing permissions
            f.writelines(["%s\n" % item for item in posList])   # loop through all the items and put them in 1 by 1