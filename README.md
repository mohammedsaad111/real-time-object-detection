# Real-Time Object Detection using YOLO

A real-time object detection application built with Python, OpenCV, and Ultralytics YOLO.

The application supports webcam and video-file input, detects objects in each frame, displays confidence scores, counts detected object classes, calculates FPS, and can save annotated images and processed videos.

## Features

- Real-time object detection using YOLO
- Webcam detection
- Video-file detection
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
│
├── input/
│   └── test video files
│
├── output/
│   └── processed videos
│
├── detector.py
├── main.py
├── utils.py
├── requirements.txt
├── .gitignore