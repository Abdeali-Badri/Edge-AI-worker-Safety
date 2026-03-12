from ultralytics import YOLO
import cv2
from playsound import playsound
import threading
import time

model = YOLO("best.pt")

cap = cv2.VideoCapture(0)

# Alarm cooldown
last_alarm_time = 0
alarm_cooldown = 3


def play_alarm():
    playsound("Alarm 2.mp3")


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.4, verbose=False)

    worker_count = 0
    no_helmet_detected = False

    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls)]

            # Count workers
            if label in ["Hardhat", "NO-Hardhat"]:
                worker_count += 1

            # Detect violation
            if label == "NO-Hardhat":
                no_helmet_detected = True

    frame = results[0].plot()

    cv2.putText(frame,
                f"Workers: {worker_count}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,255,0),
                2)

    if no_helmet_detected:
        cv2.putText(frame,
                    "WARNING: Worker without Helmet!",
                    (20,80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3)

        # Alarm with cooldown
        current_time = time.time()

        if current_time - last_alarm_time > alarm_cooldown:
            threading.Thread(target=play_alarm, daemon=True).start()
            last_alarm_time = current_time

    cv2.imshow("Worker Safety Monitor", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()