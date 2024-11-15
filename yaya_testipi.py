import cv2
import os

files = os.listdir()

imp =["y-1.jpeg","y-2.jpg","y-3.jpg"]


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for image in imp:
    img = cv2.imread(image)
    (rets, weights) = hog.detectMultiScale(img,padding=(8,8),scale=1.045)
    for (x,y,w,h) in rets:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 10)
        cv2.imshow("sonucunuz", img)


    if cv2.waitKey(0) & 0xFF == ord("q"):
        break