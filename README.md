# Real-Time Object Detection using YOLO

A real-time object detection application built with Python, OpenCV, and Ultralytics YOLO.

The application detects objects in webcam streams and video files, displays bounding boxes and confidence scores, counts detected objects by class, calculates FPS, and supports saving annotated detection images and processed videos.

## Project Preview

![AI-generated concept illustration of real-time object detection](Real-Time%20Urban%20Object%20Detection.png)

*Illustrative concept image — not an actual output screenshot from the application.*

## Features

- Real-time object detection using YOLO
- Webcam input
- Video-file input
- Confidence threshold filtering
- Bounding boxes and confidence scores
- Class-wise object counting
- Real-time FPS display
- Save annotated detection images
- Save processed detection videos

## Technologies Used

- Python
- Ultralytics YOLO
- OpenCV
- NumPy

## Project Structure

```text
real-time-object-detection/
├── input/
│   └── test video files
├── output/
│   └── processed videos
├── detector.py
├── main.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohammedsaad111/real-time-object-detection.git
cd real-time-object-detection
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application from the project directory:

```bash
python main.py
```

When prompted, select an input mode:

- Enter `1` to use your webcam.
- Enter `2` to process a video file, then provide the video file path.

During detection:
- Press `q` to quit.
- Press `s` to save an annotated detection image.

## Output

The application displays detected objects with bounding boxes and confidence scores. It can also display class-wise counts and FPS, and save annotated images or processed videos when those options are enabled.

## Learning Outcomes

This project demonstrates practical use of computer vision, object detection, video processing, and real-time inference using Python, OpenCV, and YOLO.

## Future Improvements

- Add support for image-file input
- Improve detection performance and inference speed
- Add more configuration options
- Include demonstration screenshots and sample output videos

## Author

**Mohammed Saad**

GitHub: https://github.com/mohammedsaad111
