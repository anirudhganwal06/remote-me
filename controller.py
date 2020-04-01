import zlib
import cv2
import socket
import numpy as np
import os
os.environ['DISPLAY'] = ':0'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect(("127.0.0.1", 3000))

sock.send("Controller [{}] is connected to the user!".format(
    sock.getsockname()).encode())

frameShape, x = sock.recvfrom(1024)
frameShape = np.frombuffer(frameShape, dtype=int)

size, x = sock.recvfrom(1024)
size = int(size.decode())

data = b""

while True:
    temp, userAddress = sock.recvfrom(65000)
    data += temp
    if len(data) >= size:
        frameBytes = data[:size]
        frame = np.frombuffer(frameBytes, dtype="uint8").reshape(frameShape)
        data = data[size:]
        cv2.imshow("Controller screen", frame)
        if cv2.waitKey(50) == ord('q'):
            break
    elif len(temp) == 0:
        break


cv2.destroyAllWindows()
