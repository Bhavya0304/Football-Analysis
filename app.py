from FootballAnalysisMain import Analysis
from videoUtils import VideoUtils as vu,Bbox as bb
from matplotlib import pyplot

# starting point of program
if __name__ == "__main__":
    analysis = Analysis.Analysis("./Dataset/match-1.mp4","./TrainedModel/YOLOv8.pt","./cache/detections.pkl")
    frames = vu.ReadVideoFile("./Dataset/match-1.mp4")
    result = analysis.TrackAndAnalyze("./cache/detectionsobj.pkl")
    for index,frameresult in enumerate(result):
        for player in frameresult["player"]:
            bb.ChangeBoundingBox(player["bbox"],frames[index],"ellipse",player["id"])
        for player in frameresult["referee"]:
            bb.ChangeBoundingBox(player["bbox"],frames[index],"forref")
        if("ball" in frameresult and "bbox" in frameresult["ball"]):    
            bb.BallTracker(frameresult["ball"]["bbox"],frames[index])    
    print(frames[0].shape)
    vu.SaveVideoFile(frames,"./output/output.mp4",(frames[0].shape[1],frames[0].shape[0]))
