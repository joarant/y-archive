import pandas as pd 
from os import path

videoFields = [
    "video name",
    "thumbnail",
    "id",
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
    "edit timestamp"
]

channelFields = [
    "name",
    "id",
    "sub count",
    "video count",
    "about",
    "edit timestamp"
]


def readVideoCsvFile(path):
    return pd.DataFrame(path)

# checkIfExsists
# update
# update append

def findIndexFromCsv(videoId):
    return readVideoCsvFile()['id'].loc[lambda x: x==videoId].index

# def addToCsv(data):
#     print()

def updateVideoCsv(pathToCsv, videoId, data):
    vDf = pd.read_csv(path.join(pathToCsv, "videoInfo"))
    row = vDf.loc[vDf['id'] == videoId]
    if row is None:
        print("tyhjä")
    for col in row:
        
    print()

    
def updateChannelCsv(pathToCsv, videoId, data):
    print()


def createCsvFiles(channelPath):
    vDf = pd.DataFrame(columns=videoFields)
    cDf = pd.DataFrame(columns=channelFields)
    vDf.to_csv(path.join(channelPath, "videoInfo"))
    cDf.to_csv(path.join(channelPath, "channelInfo"))
    print(vDf.columns)


# createCsvFiles()