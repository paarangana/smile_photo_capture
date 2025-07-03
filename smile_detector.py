import cv2 as cv
import time
count=0
smile_captured= False
text_start=0
text_duration=2

capture=cv.VideoCapture(1)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')

if not capture.isOpened():
    print("could not open webcam")
    exit()

while True:
    isTrue, frame=capture.read()
    if not isTrue:
        print("frame cannot be read")
        continue

    frame=cv.flip(frame,1)
    gray=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        rect_gray= gray[y:y + h, x:x + w]
        rect_colour = frame[y:y + h, x:x + w]
        
        smile = smile_cascade.detectMultiScale(rect_gray, scaleFactor=1.8, minNeighbors=20)

        if (len(smile)>0):
            if not smile_captured:
                saved = "photo_" + str(count) + ".jpg"
                cv.imwrite(saved, frame)
                smile_captured= True
                count += 1
                text_start=time.time()
                
        else:
            smile_captured= False

    if time.time()-text_start<text_duration:
        cv.putText(frame, "photo taken", (100, 100), cv.FONT_HERSHEY_PLAIN, 4, (0, 255, 0), 2)
    
    cv.imshow('smile capture',frame)

    if cv.waitKey(1) & 0xFF == ord('w'):
        break


capture.release()
cv.destroyAllWindows()


