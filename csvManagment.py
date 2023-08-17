import pandas as pd 
from os import path
from datetime import datetime

channelFieldsCols = [
    "name",
    "id",
    "sub count",
    "video count",
    "about",
    "edit timestamp"
]


videoFieldsCols = [
    "video name",
    "thumbnail",
    "id",
    "url",
    "view count",
    "upload date",
    "video",
    "audio",
    "comments",
    "description",
    "tags",
    "subtitles",
    "age restricted",
    "likes",
    "checked"
]

def readVideoCsvFile(path):
    return pd.DataFrame(path)

def getFromData(data, label: str):
    try:
        return data[label]
    except:
        return ""
        


def updateVideoCsv(pathToCsv, videoId, data):
    vDf = pd.read_csv(path.join(pathToCsv, "videoInfo.csv"))
    row = vDf.loc[vDf['id'] == videoId].index
    videoFields = {
    "video name": [getFromData(data, "title")],
    "thumbnail": [getFromData(data, "")],
    "id": [data["id"]],
    "url": [getFromData(data, "webpage_url")],
    "view count": [data["view_count"]],
    "upload date": [data["upload_date"]],
    "video": [getFromData(data, "")],
    "audio": [getFromData(data, "")],
    "comments": [getFromData(data, "")],
    "description": [data["description"]],
    "tags": [data["tags"]],
    "subtitles": [getFromData(data, "")],
    "age restricted": [data["age_limit"]],
    "likes": [data["like_count"]],
    "checked": [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
}

    if len(row) == 0:
        pdTemp = pd.DataFrame(videoFields)
        vDf = pd.concat([vDf,pdTemp], ignore_index=True, sort=False)
    else:
        pdTemp = pd.DataFrame(videoFields)
        vDf.loc[row[0]]=pdTemp.loc[0] # olit tässä

    vDf.to_csv(path.join(pathToCsv, "videoInfo.csv"), index=False)
        # id: {url, video: false, subtitles, thumbnail, audio}
    return {"id": getFromData(data, "id"), "url": getFromData(data, "webpage_url"),
            "video": getFromData(data, "video"),"subtitles": getFromData(data, "subtitles"),
            "thumbnail": getFromData(data, "thumbnail"),"audio": getFromData(data, "audio"),}
    
def updateChannelCsv(pathToCsv, videoId, data):
    cDf = pd.read_csv(path.join(pathToCsv, "channelInfo.csv"))
    
    channelFields = {
    "name": data["channel"],
    "id": data["channel_id"],
    "sub count" : data["channel_follower_count"],
    "video count": getFromData(data, ""),
    "about": getFromData(data, ""),
    "edit timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    

    pdTemp = pd.DataFrame(channelFields, index=[0])
    cDf = pd.concat([cDf,pdTemp],ignore_index=True, sort=False)
    cDf.to_csv(path.join(pathToCsv, "videoInfo.csv"), index=False)



def createCsvFiles(channelPath):
        
    vDf = pd.DataFrame(columns=videoFieldsCols)
    cDf = pd.DataFrame(columns=channelFieldsCols)
    vDf.to_csv(path.join(channelPath, "videoInfo.csv"), index=False)
    cDf.to_csv(path.join(channelPath, "channelInfo.csv"), index=False)
    print(vDf.columns)


