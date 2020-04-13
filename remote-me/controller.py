import cv2
import socket
import numpy as np
import struct
import pickle
import pyautogui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore


def startControllerDisplay(self):
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
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        qImg = QImage(frame.data, width, height,
                      bytesPerLine, QImage.Format_RGB888)
        qImg = qImg.scaled(self.widget_2.size(), QtCore.Qt.KeepAspectRatio)
        self.label_2.setPixmap(QPixmap(qImg))

def startControllerMouseControl(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 3001))

    sock.send("Controller [{}] is connected to the user!".format(
        sock.getsockname()).encode())

    data = b""
    payload_size = struct.calcsize("L")

    # Configuring pyautoui
    pyautogui.FAILSAFE = False

    while True:
        while len(data) < payload_size * 2:
            data += sock.recv(2 * payload_size)
        mousex = struct.unpack("L", data[:payload_size])[0]
        mousey = struct.unpack("L", data[payload_size:payload_size * 2])[0]
        data = data[payload_size * 2:]
        print(mousex, mousey)
        pyautogui.moveTo(mousex, mousey)
        # pyautogui.moveTo(mousex, mousey, duration=0.05)

if __name__ == "__main__":
    startController()
