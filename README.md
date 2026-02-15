# Gesture-Based Media Control

---

## About Project

**Gesture-Based Media Control** is an advanced Python application that enables users to control media playback **using hand gestures in real-time**.  

By leveraging a **webcam** and **MediaPipe Hand Tracking**, the system recognizes specific hand gestures and translates them into media commands. This allows for a **touch-free, interactive experience** suitable for accessibility, smart home media control, or Human-Computer Interaction (HCI) experiments.

Key capabilities include:

- Play / Pause  
- Next / Previous Track  
- Seek Forward / Backward  
- Volume Adjustment  
- Playback Speed Control  

This project demonstrates **computer vision, gesture recognition, and real-time interaction** in a practical application.

---

## Features

- **Real-Time Hand Gesture Detection**: Detects hand landmarks accurately using MediaPipe.  
- **Play / Pause Control**: Use gestures to start or stop media playback.  
- **Next / Previous Track**: Thumb gestures for switching tracks or videos.  
- **Seek Forward / Backward**: Wrist movement to navigate within media.  
- **Volume Control**: Adjust volume using the distance between thumb and index finger.  
- **Playback Speed Adjustment**: One to three fingers extended changes playback speed.  
- **Cooldown Mechanism**: Prevents accidental multiple triggers.  

---

## Technologies Used

- Python 3.11+  
- OpenCV  
- MediaPipe  
- NumPy  
- PyAutoGUI  
- PyCAW  
- comtypes  

---
## Preview

<img width="1022" height="456" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/d189dbbc-8836-43ed-abaa-a5f45f0b0a22" />
<img width="529" height="263" alt="image" src="https://github.com/user-attachments/assets/c8c7efc7-37ca-455b-81e4-bae7b403521e" />
<img width="675" height="246" alt="image" src="https://github.com/user-attachments/assets/9873bd9a-7dfa-4a95-a4e3-989860d028ee" />





## Installation

1. **Clone the Repository**:
2. **Install Python**:

- Make sure you have **Python 3.11+** installed.  
- You can download it from [Python Official Site](https://www.python.org/downloads/).

3. **Create a Virtual Environment** (optional but recommended):

Activate the environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install Project Dependencies:

pip install -r requirements.txt

Dependencies Included in requirements.txt
opencv-python
mediapipe
numpy
pyautogui
pycaw
comtypes


Note: Make sure your webcam is connected and accessible.

How to Run

Launch the main Python script:

python main.py


Perform gestures to control media:

Gesture	Action
4 fingers extended	Play
0 fingers extended	Pause
Thumb Up	Next Track
Thumb Down	Previous Track
Move wrist left/right	Seek Backward/Forward
1–3 fingers extended	Adjust playback speed
Distance between thumb & index	Volume control

Press Q to exit the program.

Project Structure
Gesture-Based-Media-Control/
│
├── main.py          # Main Python script with gesture detection
├── requirements.txt # Python libraries required
└── README.md        # Project documentation

Applications

Touch-free media control

Accessibility support for physically challenged users

Smart Home media systems

Human-Computer Interaction (HCI) and AI projects
