import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# ------------------- MediaPipe Setup -------------------
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# ------------------- Webcam Setup -------------------
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

# ------------------- Volume Control Setup -------------------
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

# ------------------- Gesture Variables -------------------
gesture_cooldown = 20
cooldown_counter = 0
display_text = ""
text_timer = 0
prev_x = None

# ------------------- Main Hand Detection -------------------
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cam.isOpened():
        success, image = cam.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        lmList = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
                h, w, _ = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])

        if len(lmList) != 0:
            fingers_extended = sum(lmList[i][2] < lmList[i - 2][2] for i in [8, 12, 16, 20])
            thumb_tip_y = lmList[4][2]
            thumb_base_y = lmList[2][2]
            wrist_x = lmList[0][1]

            # ------------------- Play / Pause -------------------
            if fingers_extended == 4 and cooldown_counter == 0:
                pyautogui.press('playpause')
                display_text = "Play"
                text_timer = 30
                cooldown_counter = gesture_cooldown
            elif fingers_extended == 0 and cooldown_counter == 0:
                pyautogui.press('playpause')
                display_text = "Pause"
                text_timer = 30
                cooldown_counter = gesture_cooldown

            # ------------------- Next / Previous Video -------------------
            if fingers_extended == 0 and thumb_tip_y < thumb_base_y and cooldown_counter == 0:
                pyautogui.press('nexttrack')
                display_text = "Next Video ⏭️"
                text_timer = 30
                cooldown_counter = gesture_cooldown
            elif fingers_extended == 0 and thumb_tip_y > thumb_base_y and cooldown_counter == 0:
                pyautogui.press('prevtrack')
                display_text = "Previous Video ⏮️"
                text_timer = 30
                cooldown_counter = gesture_cooldown

            # ------------------- Seek Forward / Backward -------------------
            if prev_x is not None and cooldown_counter == 0:
                movement_x = wrist_x - prev_x
                if movement_x > 150:
                    pyautogui.press('right')
                    display_text = "Seek Forward ⏩"
                    text_timer = 30
                    cooldown_counter = gesture_cooldown
                elif movement_x < -150:
                    pyautogui.press('left')
                    display_text = "Seek Backward ⏪"
                    text_timer = 30
                    cooldown_counter = gesture_cooldown
            prev_x = wrist_x

            # ------------------- Playback Speed -------------------
            if fingers_extended == 1 and cooldown_counter == 0:
                pyautogui.hotkey('shift', '<')
                display_text = "Speed: 1.0x"
                text_timer = 30
                cooldown_counter = gesture_cooldown
            elif fingers_extended == 2 and cooldown_counter == 0:
                pyautogui.hotkey('shift', '>')
                display_text = "Speed: 1.5x"
                text_timer = 30
                cooldown_counter = gesture_cooldown
            elif fingers_extended == 3 and cooldown_counter == 0:
                pyautogui.hotkey('shift', '>')
                display_text = "Speed: 2.0x"
                text_timer = 30
                cooldown_counter = gesture_cooldown

            # ------------------- Volume Control -------------------
            x1, y1 = lmList[4][1], lmList[4][2]
            x2, y2 = lmList[8][1], lmList[8][2]
            length = math.hypot(x2 - x1, y2 - y1)
            vol = np.interp(length, [50, 220], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)

            cv2.circle(image, (x1, y1), 15, (255, 255, 255), cv2.FILLED)
            cv2.circle(image, (x2, y2), 15, (255, 255, 255), cv2.FILLED)
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # ------------------- Handle Cooldowns -------------------
        if cooldown_counter > 0:
            cooldown_counter -= 1
        if text_timer > 0:
            cv2.putText(image, display_text, (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            text_timer -= 1

        # ------------------- Display the Webcam Feed -------------------
        cv2.imshow('Gesture-Based Media Control', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# ------------------- Cleanup -------------------
cam.release()
cv2.destroyAllWindows()

