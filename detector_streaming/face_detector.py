import cv2, os;

cap = cv2.VideoCapture(0);#, cv2.CAP_DSHOW);

face_detector = cv2.CascadeClassifier(
    os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
);

while True:
    ret, frame = cap.read();
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
        faces = face_detector.detectMultiScale(gray, 1.3, 5);
        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2);
        cv2.imshow("PenguinL", frame);
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break;

cap.release();
cv2.destroyAllWindows();
