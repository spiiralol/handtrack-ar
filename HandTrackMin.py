import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgFlip = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(imgFlip, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = imgFlip.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                # if id == 0:
                cv2.circle(imgFlip, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(imgFlip, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(imgFlip, f'FPS: {str(int(fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
    cv2.imshow("Image", imgFlip)

    if cv2.waitKey(33) == ord('q'):
        cv2.destroyWindows()