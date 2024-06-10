# Face Recognition System

This project is a real-time face recognition system using OpenCV and the `face_recognition` library. It detects and identifies known faces from a video feed, and saves pictures of unknown faces to an "unknown" directory every 3 seconds.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Directory Structure](#directory-structure)
* [How It Works](#how-it-works)
* [Dependencies](#dependencies)
* [License](#license)

## Installation

1. **Clone the repository:**

   ```bash
   https://github.com/MariPant/jetson-nano-securityCamera.git
   ```

2. **Install dependencies:**
   Make sure you have Python 3.6+ installed. You can install the required packages using pip:

  ```bash
   pip3 install opencv-python face_recognition numpy
   ```

3. **Prepare your images:**
   Add images of known individuals. The filenames (without extensions) will be used as names for recognition.
4. **Run the program:**

```bash
   python3 main.py
```

## Usage

* **Adding Known Faces:**
  Place images of known individuals in the `images` directory. Ensure that each image file's name corresponds to the individual's name (e.g., `name.jpg`).
* **Running the Program:**
  Execute the main script using Python:
```bash
   python3 main.py
```

* **Stopping the Program:**
  Press `Esc` to stop the video feed and exit the program.

## Directory Structure

```bash
src/
├── images/                # Directory containing known face images
├── unknown/               # Directory where images of unknown faces will be saved
├── main.py                # Main script for running the face recognition system
├── simple_facerec.py      # Module containing the SimpleFacerec class
└── README.md              # This README file
```


## How It Works

1. **Load Encoding Images:**
   The program loads images from the `images` directory and encodes them using the `face_recognition` library. These encodings are stored along with the corresponding names.
2. **Capture Video:**
   The program captures video from the default camera (you can change the source if needed).
3. **Detect Faces:**
   For each frame, it detects faces and computes their encodings. It compares these encodings with the known encodings to identify the individuals.
4. **Draw Bounding Boxes:**
   It draws bounding boxes around the faces. Green boxes are used for known faces, and red boxes are used for unknown faces. Names are displayed above the bounding boxes.
5. **Save Unknown Faces:**
   If an unknown face is detected, the program saves the image of the face to the `unknown` directory every 3 seconds.

## Dependencies

* Python 3.6+
* OpenCV
* face_recognition
* numpy

You can install these dependencies using pip:
```bash
pip3 install opencv-python face_recognition numpy
```
