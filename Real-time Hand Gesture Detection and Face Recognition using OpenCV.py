import cv2
import numpy as np
import time

def detect_skin_color_hsv(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 48, 80], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    return mask

def count_fingers(contour, drawing):
    hull = cv2.convexHull(contour, returnPoints=False)
    if hull is not None and len(hull) > 3:
        defects = cv2.convexityDefects(contour, hull)
        if defects is not None:
            cnt = 0
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])
                a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                angle = np.arccos((b**2 + c**2 - a**2) / (2*b*c))
                if angle <= np.pi / 2:
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return True, cnt
    return False, 0

print("Starting program...")

cap = cv2.VideoCapture(0)  # Change the camera index as needed

if not cap.isOpened():
    print("Error: Webcam not accessible")
else:
    print("Webcam successfully accessed.")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
prev_frame_time = time.time()
hand_positions = {}
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

running = True

while running:
    try:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame from webcam. Exiting...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        skin_mask = detect_skin_color_hsv(frame)
        contours, _ = cv2.findContours(skin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i, contour in enumerate(contours):
            if cv2.contourArea(contour) > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                hand_roi = frame[y:y+h, x:x+w]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                fingers = count_fingers(contour, hand_roi)

                if fingers[0]:
                    cv2.putText(frame, str(fingers[1]), (x + 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                color = colors[i % len(colors)]
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    cv2.circle(frame, (cx, cy), 5, color, -1)

                    if i in hand_positions:
                        hand_positions[i].append((cx, cy))
                        for j in range(1, len(hand_positions[i])):
                            cv2.line(frame, hand_positions[i][j - 1], hand_positions[i][j], color, 2)
                    else:
                        hand_positions[i] = [(cx, cy)]

        # FPS calculation
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('frame', frame)

        # Exit strategy
        if cv2.waitKey(1) == 27:  # ESC key
            running = False

    except Exception as e:
        print(f"Error: {str(e)}")

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Program ended.")
