# Real-Time Audio and Video Monitoring with Dice Roll Detection and Probability Calculation
## Overview
This project is a Python-based development that monitors audio and video in real-time. Whenever a specific audio is detected, the system automatically takes a screenshot of the video feed and analyzes it to determine if dice rolls are present on the screen. If dice rolls are detected, the program calculates the probabilities of the next dice rolls based on the detected numbers.

## Features
Real-time Audio Monitoring: Continuously listens for a specific audio cue.
Automated Screenshot Capture: Captures a screenshot whenever the specified audio is detected.
Dice Roll Detection: Analyzes the captured screenshot to identify dice rolls.
Probability Calculation: Computes the probabilities of future dice rolls based on detected numbers.
Highly Customizable: Easily adaptable to monitor different audio cues and screen elements.
## Requirements
To run this project, you will need the following dependencies:

Python 3.x
OpenCV (cv2)
NumPy
Pyaudio
Scikit-image
TensorFlow or PyTorch (optional, for advanced image recognition)
Matplotlib (for visualizing dice roll probabilities)
Other relevant libraries as per your project setup
