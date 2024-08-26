from FootballAnalysisMain import Analysis

# starting point of program
if __name__ == "__main__":
    analysis = Analysis.Analysis("./Dataset/match-1.mp4","./cache/detections.pkl")
    result = analysis.GetDetections()
    print(result)