import cv2
import os

files = os.listdir()



hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


a = int(input("kaçıncı kayot sayıyla yaz: "))
# Video kaydı için dosya adı ve formatı belirle
filename = f'video_kayit{a}.avi'
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
resolution = (640, 480)

# Video yakalama ve yazıcı nesnelerini oluştur
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter(filename, codec, fps, resolution)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Görüntüyü kaydet
        out.write(frame)



for ret in frame:
    img = cv2.imread(ret)
    (rets, weights) = hog.detectMultiScale(img,padding=(8,8),scale=1.045)
    for (x,y,w,h) in rets:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 10)
        cv2.imshow("sonucunuz", img)

        # Görüntüyü ekranda göster


        # 'q' tuşuna basıldığında döngüyü kır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



