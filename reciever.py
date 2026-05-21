import cv2
import socket
import numpy as np
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5005))
while True:
    data, _ = sock.recvfrom(65536)
    npdata = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Video", edges)
    if cv2.waitKey(1) == ord('q'):
        break
sock.close()
cv2.destroyAllWindows()