import cv2
import socket

UDP_IP = "127.0.1.11"
UDP_PORT = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

        xpoint = int(x+w/2)
        ypoint = int(y+h/2)

        
        xp=(-(xpoint-320)*(3.7/320))
        # xp = round(xp,2)
        yp=(-(ypoint-320)*(3.7/320))
        # yp = 2+round(xp,2)
        print(xp,yp)

        lookatmyfaceXY = str(xp) + "," + str(yp)
        # print(lookatmyfaceXY)
        sock.sendto(bytes(lookatmyfaceXY, "utf-8"), (UDP_IP, UDP_PORT))

        cv2.circle(img, (xpoint,ypoint), 2, (0, 0, 255), -1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
