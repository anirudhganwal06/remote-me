import numpy as np
import socket
import cv2
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect(("127.0.0.1", 3000))

sock.send("Controller [{}] is connected to the user!".format(sock.getsockname()).encode())

# out = cv2.VideoWriter(
#     "recorder.mkv", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (1920, 1080))

size, x = sock.recvfrom(1024)
size = int(size.decode())
print(size)

index = 1
data = b""
while True:
  temp, userAddress = sock.recvfrom(65507)
  # print(data.__sizeof__())
  if (temp.__sizeof__() == 0):
    break
  data += temp
  if data.__sizeof__() < size:
    continue
  else:
    frame = pickle.loads(data[:size])
    cv2.imwrite("ss{}.jpg".format(index), frame)
    index += 1
    data = data[size:]
    # break
    
  # out.write(frame)