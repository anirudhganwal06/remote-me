import zlib
import socket
import cv2
import mss
import time
import numpy as np
import os
os.environ['DISPLAY'] = ":0"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 3000))
print("User hosting screen at port {}".format(3000))

data, controllerAddress = sock.recvfrom(1024)
print(data.decode())

firstTime = True
bufferSize = 65000
with mss.mss() as sct:
    width = 200
    height = 100
    monitor = {"top": 0, "left": 0, "width": width, "height": height}

    while True:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        frameBytes = frame.tobytes()
        if firstTime:
            firstTime = False
            frameShape = np.array(frame.shape).tobytes()
            sock.sendto(frameShape, controllerAddress)
            sock.sendto(str(len(frameBytes)).encode(), controllerAddress)

        while len(frameBytes) > 0:
            if len(frameBytes) < bufferSize:
                sock.sendto(frameBytes, controllerAddress)
                break
            else:
                sock.sendto(frameBytes[:bufferSize], controllerAddress)
                frameBytes = frameBytes[bufferSize:]
        cv2.imshow("User Screen", frame)
        if cv2.waitKey(50) == ord('q'):
            break
        # time.sleep(0.05)


# cv2.destroyAllWindows()
