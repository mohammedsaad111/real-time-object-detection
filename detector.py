from ultralytics import YOLO


class ObjectDetector:
    def __init__(self, model_path="yolo26n.pt", confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        return self.model(frame, conf=self.confidence)

    def get_class_counts(self, results):
        class_counts = {}

        for class_id in results[0].boxes.cls:
            class_name = self.model.names[int(class_id)]
            class_counts[class_name] = class_counts.get(class_name, 0) + 1

        return class_counts

    def annotate(self, results):
        return results[0].plot()