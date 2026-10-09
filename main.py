from ultralytics import YOLO
import cv2

from detector import ObjectDetector
from utils import calculate_fps, draw_information


# Create the object detector
detector = ObjectDetector(
    model_path="yolo26n.pt",
    confidence=0.5
)

# Choose input mode
print("Choose input:")
print("1. Webcam")
print("2. Video file")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    source = 0

elif choice == "2":
    source = input("Enter the video file path: ")

else:
    print("Invalid choice.")
    exit()


# Open the video source
cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print("Could not open the selected source.")
    exit()


# Set up video writer
video_writer = None

if choice == "2":
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = "output/detected_video.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    video_writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )


# FPS tracking
previous_time = 0


while True:

    ret, frame = cap.read()

    if not ret:
        print("End of video or unable to read frame.")
        break


    # Run object detection
    results = detector.detect(frame)


    # Get object counts
    class_counts = detector.get_class_counts(results)


    # Draw YOLO detections
    annotated_frame = detector.annotate(results)


    # Calculate FPS
    fps, previous_time = calculate_fps(previous_time)


    # Draw FPS and object counts
    annotated_frame = draw_information(
        annotated_frame,
        fps,
        class_counts
    )


    # Save processed video frame
    if video_writer is not None:
        video_writer.write(annotated_frame)


    # Display result
    cv2.imshow(
        "Real-Time Object Detection",
        annotated_frame
    )


    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):

        cv2.imwrite(
            "output/detection_result.jpg",
            annotated_frame
        )

        print(
            "Detection result saved as output/detection_result.jpg"
        )

    elif key == ord("q"):
        break


# Release resources
cap.release()

if video_writer is not None:
    video_writer.release()

cv2.destroyAllWindows()