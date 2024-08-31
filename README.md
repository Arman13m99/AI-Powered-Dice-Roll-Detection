# Real-Time Audio and Video Monitoring with Dice Roll Detection and Probability Calculation

## Overview
This project is a Python-based development that monitors audio and video in real-time. Whenever a specific audio is detected, the system automatically takes a screenshot of the video feed and analyzes it to determine if dice rolls are present on the screen. If dice rolls are detected, the program calculates the probabilities of the next dice rolls based on the detected numbers.

## Features
- **Real-time Audio Monitoring**: Continuously listens for a specific audio cue.
- **Automated Screenshot Capture**: Captures a screenshot whenever the specified audio is detected.
- **Dice Roll Detection**: Analyzes the captured screenshot to identify dice rolls.
- **Probability Calculation**: Computes the probabilities of future dice rolls based on detected numbers.
- **Highly Customizable**: Easily adaptable to monitor different audio cues and screen elements.

## Requirements
To run this project, you will need the following dependencies:

- **Python 3.8**
- **OpenCV (`cv2`)**
- **NumPy**
- **Pyaudio**
- **Scikit-image**
- **TensorFlow or PyTorch** (optional, for advanced image recognition)
- **Matplotlib** (for visualizing dice roll probabilities)
- **Other relevant libraries as per your project setup**

## Usage
### Start Monitoring:
- Run the `main.py` file to start the real-time monitoring.
- The system will continuously listen for the specified audio cue.

### Dice Roll Detection:
- Once the specific audio is detected, a screenshot is captured.
- The system will analyze the screenshot to detect dice rolls.
- The detected dice values will be used to calculate the probabilities of future rolls.

### View Results:
- Probability results will be displayed in the console.
- If configured, the results can also be visualized using Matplotlib.

## Example
Here’s an example of how the system works:

- The system detects an audio cue (e.g., a bell sound).
- A screenshot is automatically taken.
- The system identifies dice with values 3 and 5 on the screen.
- It calculates the probability of the next dice roll (e.g., the probability of rolling a 4 next is 16.67%).

## Note
Due to the large size of the trained models, they could not be uploaded to this repository. If you need the latest trained models for both audio and video detection, please contact me at **arman13m99@gmail.com** to request access.
