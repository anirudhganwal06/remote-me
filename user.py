import struct
import pickle
import socket
import cv2
import mss
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore


def startUser(self):
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
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
            frameBytes = pickle.dumps(frame)
            sock.sendall(struct.pack("L", len(frameBytes)) + frameBytes)
            height, width, channel = frame.shape
            bytesPerLine = 3 * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            qImg = qImg.scaled(self.widget.size(), QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(QPixmap(qImg))

    cv2.destroyAllWindows()

if __name__ == "__main__":
    startUser()
