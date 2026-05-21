import cv2
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    sock.sendto(buffer.tobytes(), ("127.0.0.1", 5005))
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
sock.close()
cv2.destroyAllWindows()