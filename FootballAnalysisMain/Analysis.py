from Detection import detection
import pickle

class Analysis:
    def __init__(self,file,getFromCache = None):
        self.filePath = file
        self.model = detection
        if(getFromCache == None):
            self.fromcache = False
        else:
            self.fromcache = True
        self.CacheFilePath = getFromCache        

    def SaveDetections(self):
        with open(self.CacheFilePath,'wb+') as f:
            pickle.dump(self.detections, f)

    def GetFromCache(self):
        try:
            with open(self.CacheFilePath,'rb') as f:
                return (True,pickle.load(f))    
        except Exception as e:
            print(e)
            return (False,None)

    def GetDetections(self):
        if(self.fromcache):
            result = self.GetFromCache()
            if(result[0]):
                self.detections = result[1]
            else:
                self.detections = self.model.DetectObjects(self.filePath)     
            self.SaveDetections()
        else:
            self.detections = self.model.DetectObjects(self.filePath)
        
        return self.detections