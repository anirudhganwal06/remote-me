import os
os.environ['DISPLAY'] = ":0"
import pickle
import socket
from PIL import Image
import cv2
import pyautogui
import time
import numpy as np


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 3000))
print("User hosting screen at port {}".format(3000))

data, controllerAddress = sock.recvfrom(1024)
print(data.decode())

firstTime = True
bufferSize = 15000
while True:
    frame = np.array(pyautogui.screenshot(region=(0, 0, 200, 400)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frameBytes = pickle.dumps(frame)
    print(frameBytes.__sizeof__())
    if firstTime:
        firstTime = False
        size = frameBytes.__sizeof__()
        sock.sendto(str(size).encode(), controllerAddress)

    while frameBytes.__sizeof__() > 0:
        # print(frameBytes.__sizeof__())
        if frameBytes.__sizeof__() < bufferSize:
            sock.sendto(frameBytes, controllerAddress)
            break
        else:
            # print(frameBytes.__sizeof__())
            sock.sendto(frameBytes[:bufferSize], controllerAddress)
            frameBytes = frameBytes[bufferSize:]

    time.sleep(0.05)
    break

#     # cv2.imshow("Screen Recorder", frame)
#     # if cv2.waitKey(50) == ord('q'):
#     #     break

# cv2.destroyAllWindows()
