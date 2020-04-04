import cv2
import socket
import numpy as np
import struct
import pickle

def startController():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 3000))

    sock.send("Controller [{}] is connected to the user!".format(
        sock.getsockname()).encode())

    data = b""
    payload_size = struct.calcsize("L")
    print(payload_size)

    while True:
        data += sock.recv(payload_size)
        packedMessageSize = data[:payload_size]
        data = data[payload_size:]
        messageSize = struct.unpack("L", packedMessageSize)[0]
        while len(data) < messageSize:
            data += sock.recv(65000)
        frameData = data[:messageSize]
        data = data[messageSize:]
        frame = pickle.loads(frameData)
        cv2.imshow("Controller screen", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    startController()