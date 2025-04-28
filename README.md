# 🚨 **Women SOS Gesture Recognition System**

## 🌟 **Overview**

The **Women SOS Gesture Recognition System** is an innovative and lifesaving project designed to detect distress signals from women in emergency situations using hand gestures. This system uses **MediaPipe** for precise hand landmark tracking and **OpenCV** for real-time video processing, enabling automatic detection of SOS gestures. The system identifies when a woman forms the SOS distress signal by closing her thumb towards the palm and repeatedly opening and closing her fingers. When the gesture is detected, an SOS alert is triggered on the screen.

This project is intended to provide a discreet and intuitive safety tool for women, helping them signal for help during emergencies without the need for a phone or voice command.

---

## 🛠️ **Key Features**

- **Real-Time Hand Tracking**: Leverages **MediaPipe** to track hand movements in real time.
- **SOS Gesture Recognition**: Detects the internationally recognized SOS distress signal by monitoring thumb and finger movements.
- **SOS Alert System**: Triggers an on-screen SOS warning when the gesture is detected.
- **Automatic Reset**: If no further movement is detected, the SOS signal resets after a predefined timeout period.
- **Base Script for Reference**: This is a foundational script, designed for experimentation and as a reference point to build more sophisticated systems.

---

## ⚙️ **Requirements**

Before you run the system, ensure you have Python 3.x and the following libraries installed:

- **Python 3.x**
- **OpenCV** (for image processing)
- **MediaPipe** (for hand tracking)
- **NumPy** (for numerical calculations)

### 📥 **Install Dependencies**

To get started, simply install the required libraries by running:

```bash
pip install opencv-python mediapipe numpy
```

---

## 🚀 **How to Use**

1. **Clone the Repository**: Clone this repository to your local machine to get started.

   ```bash
   git clone https://github.com/Ayushskull7/Women-SOS-Gesture-Recognition.git
   ```

2. **Run the Script**: After cloning the repository, navigate to the project folder and run the Python script to begin gesture detection.

   ```bash
   python sos_gesture_recognition.py
   ```

3. **Perform the SOS Gesture**: In front of your camera, form the SOS gesture by closing your thumb towards your palm and repeatedly opening and closing your fingers.

4. **SOS Signal Detection**: If the system detects the SOS gesture, it will display the message **"SOS Signal Detected!"** on the screen.

5. **Exit the Application**: To exit, simply press the **'q'** key.

---

## 🧠 **How It Works**

The system operates by tracking 21 hand landmarks in real time using **MediaPipe**. Here's how the SOS gesture is recognized:

1. **Thumb Closed to Palm**: The system checks if the thumb is closed towards the palm, indicating the "fist" gesture.
2. **Finger Movement**: The system monitors the fingers for any repeated opening and closing, which is key to recognizing the SOS gesture.
3. **SOS Trigger**: Once both conditions (thumb closed + repeated finger movement) are met, the system triggers the SOS alert.

---

## 🔨 **Future Enhancements & Ongoing Improvements**

This system is a **base script** designed for experimentation. Future development and improvements are underway, including:

- **Multi-Threading Support**: The system will be enhanced with multi-threading to ensure smoother real-time detection and efficient processing, especially for higher frame rates.
- **Multi-Device Support**: We're working on making the system compatible with multiple devices simultaneously, enabling broader deployment.
- **API Setup**: An API is being developed to integrate the SOS detection system with other applications and services.
- **Mobile App Integration**: Plans to port this solution to mobile devices, allowing for easy on-the-go SOS gesture detection.
- **Enhanced Gesture Recognition**: The model's accuracy will be improved, and more emergency gestures will be added for better flexibility.
- **Alert System Enhancements**: Future releases will include SMS/Email notification systems for sending alerts when the SOS gesture is detected.
- **Cross-Platform Compatibility**: The system will be tested and optimized for multiple platforms to ensure it's accessible to a wide range of users.

---

## 🚧 **Disclaimer**

This project is in its **early stages**, and the current implementation serves as a reference script. Improvements and optimizations are ongoing, and new features will be added in upcoming releases.

Stay tuned for more updates as we work towards building a fully-featured and reliable Women SOS Gesture Recognition system!

---
