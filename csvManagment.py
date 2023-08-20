import pandas as pd 
from os import path, listdir
from datetime import datetime
import json

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

def getFromData(data, label: str):
    try:
        return data[label]
    except:
        return ""
        

def updateVideoCsv(pathToCsv, pathToFolder):

    paths = getPaths(pathToFolder)
    file = open(paths["info_path"])
    data = json.load(file)
    vDf = pd.read_csv(pathToCsv)

    row = vDf.loc[vDf['id'] == getFromData(data, "id")].index
    videoFields = {
    "video name": [getFromData(data, "title")],
    "thumbnail": [getFromData(paths, "thumbnail_path")],
    "id": [getFromData(data, "id")],
    "url": [getFromData(data, "webpage_url")],
    "view count": [getFromData(data, "view_count")],
    "upload date": [getFromData(data, "upload_date")],
    "video": [getFromData(paths, "video_path")],
    "audio": [getFromData(paths, "audio_path")],
    "comments": [getFromData(paths, "comments_path")],
    "description": [getFromData(data, "description")],
    "tags": [getFromData(data, "tags")],
    "subtitles": [getFromData(paths, "subtitles_path")],
    "age restricted": [getFromData(data, "age_limit")],
    "likes": [getFromData(data, "like_count")],
    "checked": [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    }

    if len(row) == 0:
        pdTemp = pd.DataFrame(videoFields)
        vDf = pd.concat([vDf,pdTemp], ignore_index=True, sort=False)
    else:
        pdTemp = pd.DataFrame(videoFields)
        vDf.loc[row[0]]=pdTemp.loc[0]


    vDf.to_csv(pathToCsv, index=False)
    return {"id": getFromData(data, "id"), "url": getFromData(data, "webpage_url"),
            "video": getFromData(paths, "video_path"),"subtitles": getFromData(paths, "subtitles_path"),
            "thumbnail": getFromData(paths, "thumbnail_path"),"audio": getFromData(paths, "audio_path"),}
    
def updateChannelCsv(pathToCsv, data):
    cDf = pd.read_csv(pathToCsv)
    
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
    cDf.to_csv(pathToCsv, index=False)



def createCsvFiles(channelPath):
        
    vDf = pd.DataFrame(columns=videoFieldsCols)
    cDf = pd.DataFrame(columns=channelFieldsCols)
    vDf.to_csv(path.join(channelPath, "videoInfo.csv"), index=False)
    cDf.to_csv(path.join(channelPath, "channelInfo.csv"), index=False)


def getPaths(folder):

    fileRecognition = {
                "info_path": [".info.json"],
                "comments_path":["comments.json"],
                "thumbnail_path":[".webp"],
                "video_path":[".webm"],
                "audio_path":[".m4a"],
                "subtitles_path":[".vtt"],
                }

    filePaths = {
                "info_path": "",
                "comments_path":"",
                "thumbnail_path":"",
                "video_path":"",
                "audio_path":"",
                "subtitles_path":"",
                }

    for vFile in listdir(folder):
        for k in fileRecognition:
            for idString in fileRecognition[k]:
                if idString in vFile:
                    filePaths[k] = path.join(folder, vFile)

    return filePaths
