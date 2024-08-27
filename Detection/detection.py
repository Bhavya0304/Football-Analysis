from ultralytics import YOLO
import time

def DetectObjects(videoPath,modelPath = None):
    if(modelPath == None):
        model = YOLO("yolov8x")
    else:
        model = YOLO(modelPath)    
    result = model.predict(videoPath,save=True)
    return result

