import cv2
import socket
import pickle
import numpy as np
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Receiver with Canny Edge Detection start")
while True:
    data, addr = sock.recvfrom(65536)
    buffer = pickle.loads(data)
    frame = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    cv2.imshow("Canny Edge Detection", edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
sock.close()
cv2.destroyAllWindows()