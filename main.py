import cv2
import mediapipe as mp
import numpy as np
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

THUMB_TIP = 4
INDEX_TIP = 8
MIDDLE_TIP = 12
RING_TIP = 16
PINKY_TIP = 20
PALM_BASE = 0
WRIST = 0
MIDDLE_FINGER_MCP = 9

sos_warning = False
gesture_start_time = None
finger_open_close_state = None
finger_movement_tolerance = 0.05
movement_counter = 0
required_cycles = 2
movement_reset_time = 1.5


def calculate_distance(landmark1, landmark2):
    return np.sqrt(
        (landmark1.x - landmark2.x) ** 2 + (landmark1.y - landmark2.y) ** 2 + (landmark1.z - landmark2.z) ** 2)


def calculate_hand_size(landmarks):
    wrist = landmarks[WRIST]
    middle_finger_tip = landmarks[MIDDLE_TIP]
    return calculate_distance(wrist, middle_finger_tip)


def is_thumb_closed_to_palm(landmarks):
    thumb_tip = landmarks[THUMB_TIP]
    palm_base = landmarks[PALM_BASE]
    middle_finger_mcp = landmarks[MIDDLE_FINGER_MCP]
    hand_size = calculate_hand_size(landmarks)
    normalized_thumb_distance = calculate_distance(thumb_tip, middle_finger_mcp) / hand_size
    return normalized_thumb_distance < 0.2


def are_fingers_opening_closing(landmarks, prev_states):
    fingers_moving = False
    finger_tips = [landmarks[INDEX_TIP], landmarks[MIDDLE_TIP], landmarks[RING_TIP], landmarks[PINKY_TIP]]
    palm_base = landmarks[PALM_BASE]
    current_distances = [calculate_distance(finger_tip, palm_base) for finger_tip in finger_tips]
    if prev_states is not None:
        fingers_moving = any(
            abs(current - prev) > finger_movement_tolerance for current, prev in zip(current_distances, prev_states))
    return current_distances, fingers_moving


cap = cv2.VideoCapture(0)

last_finger_movement_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb_closed = is_thumb_closed_to_palm(hand_landmarks.landmark)
            current_finger_state, fingers_moving = are_fingers_opening_closing(hand_landmarks.landmark,
                                                                               finger_open_close_state)

            if thumb_closed:
                if fingers_moving:
                    last_finger_movement_time = time.time()
                    if movement_counter < required_cycles:
                        movement_counter += 1
                        print(f"Finger movement cycle detected: {movement_counter}")

                    if movement_counter >= required_cycles and not sos_warning:
                        gesture_start_time = time.time()
                        sos_warning = True
                        print("SOS Signal Detected!")

            if sos_warning and (time.time() - last_finger_movement_time > movement_reset_time):
                sos_warning = False
                movement_counter = 0
                print("SOS Signal Reset")

            finger_open_close_state = current_finger_state

    if sos_warning:
        cv2.putText(frame, 'SOS Signal Detected!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('SOS Gesture Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
