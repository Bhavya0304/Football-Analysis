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

def SaveVideoFile(frames,path,size):
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(path,fourcc,24,size)
    for frame in frames:
        writer.write(frame)
    writer.release()  

def CreateEllipse(frame,center,axes,angle,start_angle,end_angle,color,thickness):
    cv2.ellipse(frame,center,axes,angle,start_angle,end_angle,color,thickness,cv2.LINE_4)

def CreateRectangle(frame,topcorner,bottoncorner,color):
    cv2.rectangle(frame,topcorner,bottoncorner,color,cv2.FILLED)

def PutText(frame,text,point,color,scale = 1.5):
    cv2.putText(frame, text, point, fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale=scale, color=color)

def CreateTriangle(frame,point,color):
    cv2.fillPoly(frame,point,color)
        
