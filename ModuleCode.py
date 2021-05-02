  import cv2
  import mediapipe as mp
  import time
  import HandTrackModule as htm
  
  cap = cv2.VideoCapture(0)
  detector = htm.handDetector()
  pTime = 0
  cTime = 0

  while True:
      success, img = cap.read()
      img = detector.findHands(img)
      lmList = detector.findPosition(img)
      if len(lmList) != 0:
          print(lmList[4])

      imgFlip = cv2.flip(img, 1)

      cTime = time.time()
      fps = 1/(cTime-pTime)
      pTime = cTime

      cv2.putText(imgFlip, f'FPS: {str(int(fps))}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
      cv2.imshow("HandTrack AR", imgFlip)

      if cv2.waitKey(33) == ord('q'):
          cv2.destroyWindows()
