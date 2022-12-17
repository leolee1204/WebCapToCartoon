from cartoon import *
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    cartoon = handle(frame)
    out.write(cartoon)
    cv2.imshow('cartoon', cartoon)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()