#https://github.com/Casualflemingo/Face-detection-and-recognition.git

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
        rate,frame = cap.read()

        cv2.imshow("test",frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
