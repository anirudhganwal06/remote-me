import struct
import pickle
import socket
import cv2
import mss
import numpy as np
import os
os.environ['DISPLAY'] = ":0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 3000))
print("User hosting screen at port {}".format(3000))
s.listen()

sock, controllerAddress = s.accept()

data = sock.recv(1024)
print(data.decode())

firstTime = True
bufferSize = 65000
with mss.mss() as sct:
    width = 1920
    height = 1080
    monitor = {"top": 0, "left": 0, "width": width, "height": height}
    while True:
        frame = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        frameBytes = pickle.dumps(frame)
        sock.sendall(struct.pack("L", len(frameBytes)) + frameBytes)
        cv2.imshow("User Screen", frame)
        if cv2.waitKey(50) == ord('q'):
            break

cv2.destroyAllWindows()
