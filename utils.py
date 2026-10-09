import cv2
import time


def calculate_fps(previous_time):
    current_time = time.time()

    if previous_time == 0:
        fps = 0
    else:
        fps = 1 / (current_time - previous_time)

    return fps, current_time


def draw_information(frame, fps, class_counts):
    # Display FPS
    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display detected object counts
    y_position = 80

    for class_name, count in class_counts.items():
        cv2.putText(
            frame,
            f"{class_name}: {count}",
            (20, y_position),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        y_position += 30

    return frame