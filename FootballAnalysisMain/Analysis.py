from Detection import detection
import pickle
import supervision as sv
import torch as pt


class Analysis:
    def __init__(self,file,modelPath = None,getFromCache = None):
        self.filePath = file
        self.model = detection
        self.modelPath = modelPath
        self.tracker = sv.ByteTrack()
        if(getFromCache == None):
            self.fromcache = False
        else:
            self.fromcache = True
        self.CacheFilePath = getFromCache        

    def SaveDetections(self,filepath,obj):
        with open(filepath,'wb+') as f:
            pickle.dump(obj, f)
        return obj

    def GetFromCache(self,filepath):
        try:
            with open(filepath,'rb') as f:
                return (True,pickle.load(f))    
        except Exception as e:
            print(e)
            return (False,None)

    def GetDetections(self):
        if(self.fromcache):
            result = self.GetFromCache(self.CacheFilePath)
            if(result[0]):
                self.detections = result[1]
            else:
                self.detections = self.model.DetectObjects(self.filePath,modelPath=self.modelPath)     
                self.SaveDetections(self.CacheFilePath,self.detections)
        else:
            self.detections = self.model.DetectObjects(self.filePath,self.modelPath)
        
        return self.detections

    def TrackAndAnalyze(self,CachePath = None):
        detectionobj = None
        if(CachePath == None):
            detections = self.GetDetections()
            detectionobj = self.GetTrackerDetectionsObject(detections)
            self.SaveDetections(CachePath,detectionobj)
        else:
            isobj,detectionobj = self.GetFromCache(CachePath)
            if(isobj):
                return detectionobj
            else:
                detections = self.GetDetections()
                detectionobj = self.GetTrackerDetectionsObject(detections)
                self.SaveDetections(CachePath,detectionobj)
        return detectionobj

    def GetTrackerDetectionsObject(self,detections):
        detectionobj = []

        for frame_num,detection in enumerate(detections):
            detection_supervision = sv.Detections.from_ultralytics(detection)
            inv_cls = {detection.names[k]:k for k in detection.names }
            detectionobj.append({})
            detectionobj[frame_num]["player"] = []
            detectionobj[frame_num]["referee"] = []
            detectionobj[frame_num]["ball"] = {}
            for i,class_a in enumerate(detection_supervision.class_id):
                if(detection.names[class_a] == "goalkeeper"):
                    detection_supervision.class_id[i] = inv_cls["player"]
            detection_with_track = self.tracker.update_with_detections(detection_supervision)

            for i,bbox in enumerate(detection_with_track.xyxy):
                if(detection_with_track.class_id[i] == inv_cls["ball"]):
                    detectionobj[frame_num]["ball"] = {"id":detection_with_track.tracker_id[i],"bbox": bbox}
                if(detection_with_track.class_id[i] == inv_cls["player"]):
                    detectionobj[frame_num]["player"].append({"id":detection_with_track.tracker_id[i],"bbox": bbox})
                if(detection_with_track.class_id[i] == inv_cls["referee"]):
                    detectionobj[frame_num]["referee"].append({"id":detection_with_track.tracker_id[i],"bbox": bbox})
        return detectionobj