import cv2

def ReadVideoFile(path):
    frames = []
    video = cv2.VideoCapture(path)
    while(video.isOpened()):
        isframe,frame = video.read()
        frames.append(frame)
        if isframe == False:
            break
    video.release()
    return frames    