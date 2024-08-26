from ultralytics import YOLO
import time

def DetectObjects(videoPath):
    model = YOLO("yolov8x")
    result = model.predict(videoPath,save=True)
    return result

