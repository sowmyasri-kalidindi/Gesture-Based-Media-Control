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

## Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/YourUsername/Gesture-Based-Media-Control.git
cd Gesture-Based-Media-Control
