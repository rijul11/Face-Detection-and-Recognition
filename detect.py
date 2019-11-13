import cv2
import face_recognition

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

frames = []

while (True):

    ret, frames = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(gray, 1.1, 1 )
        # flags = cv2.CV_HAAR_SCALE_IMAGE

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        color = (0, 255, 0)
        stroke = 2
        endx = x+w
        endy = y+h
        cv2.rectangle(frames, (x, y), (endx, endy), color, stroke)
    # break #comment break to allow more rectangles

    # Display the resulting frame and stats
    print("Found {0} faces".format(len(faces)))
    cv2.imshow('frames', frames)

    # Exit if ESC pressed
    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()