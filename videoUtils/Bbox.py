from videoUtils.videoutilsmain import CreateEllipse,PutText,CreateRectangle,CreateTriangle
import numpy as np

def BallTracker(bbox,frame):
    x1,y1,x2,y2 = bbox
    y1 = y1 - 20
    length_trig = 10
    center = int((x1+x2)/2)
    points = np.array([[[int(center - length_trig),int(y1 + length_trig)],[int(center + length_trig),int(y1 + length_trig)],[center,int(y1)]]]).astype(np.int32)
    CreateTriangle(frame,points,(0,255,0))

def ChangeBoundingBox(bbox,frame,shape,playerid = None):
    if shape == "ellipse":
        x1,y1,x2,y2 = bbox
        xcenter = int((x1 + x2)/2)
        center = (xcenter,int(y2))
        axis = (int(x2-x1),int((x2-x1)*0.35))
        angle = 0
        start_angle = -45
        end_angle = 235
        color = (255,255,0)
        thickness = 2
        CreateEllipse(frame,center,axis,angle,start_angle,end_angle,color,thickness)
        # for the text
        minorlength= int(int((x2-x1)*0.35)/2)
        rectangle_height = 15
        recangle_width = 25
        axislength = int((x2-x1)*0.35)

        x1_rect = int(xcenter - (recangle_width/2))
        x2_rect = int(xcenter + (recangle_width/2))
        y1_rect = int(y2 + (axislength / 2) - (rectangle_height/2))
        y2_rect = int(y2 + (axislength / 2) + (rectangle_height/2))
        CreateRectangle(frame,(x1_rect,y1_rect),(x2_rect,y2_rect),(255,255,0))
        PutText(frame,str(playerid),(xcenter - 8,int(y2 + 5 + (axislength / 2))),(0,0,255),0.4)
    elif shape == "forref":
        x1,y1,x2,y2 = bbox
        xcenter = int((x1 + x2)/2)
        center = (xcenter,int(y2))
        axis = (int(x2-x1),int((x2-x1)*0.35))
        angle = 0
        start_angle = -45
        end_angle = 235
        color = (0,255,255)
        thickness = 2
        CreateEllipse(frame,center,axis,angle,start_angle,end_angle,color,thickness)
    return frame