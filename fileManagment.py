# create folders
# report file status
import os
from os import path, access, W_OK, R_OK
import errno
import sys
import csvManagment as cm

# tree
# channelName
    # csv videoes
    # csv channel
    # content folder
        # video file
        # audio file
        # other files


def createChannelFolder(channelName: str, parentPath):
    path = os.path.join(parentPath, channelName)
    try:
        os.mkdir(path)
        return path
    except OSError as error:
        print(error)
        
def createVideoFolder(videoName: str, parentPath: str):
    path = os.path.join(parentPath, videoName)
    try:
        os.mkdir(path)
    except OSError as error: 
        print(error)
        
def clearTemp():
    for file in os.listdir("tempFileLocation"):
        os.remove(os.path.join("tempFileLocation",file))

def moveFiles(from_folder, dest_folder):
    for vFile in os.listdir(from_folder):
        if checkIfExsists(os.path.join(dest_folder, vFile)):
            os.rename(os.path.join(from_folder, vFile), os.path.join(dest_folder, vFile))
        else:
            os.replace(os.path.join(from_folder, vFile), os.path.join(dest_folder, vFile))
       


def checkIfExsists(file_path):
    return os.path.exists(file_path)

def getPath(filePath):
    return path.join(path.dirname(path.realpath(__file__)), filePath)

def getFolderPath(folderPath):
    folder = folderPath
    if folder is None:
        folder = ""
    if not folder == "" and folder[len(folder)-1]:
        folder += "/"
    return path.join(path.dirname(path.realpath(__file__)), folder)


def checkFolderPath(filePath):
    if not path.exists(getFolderPath(filePath)): 
        print(filePath,"invalid path")
        return False
    if not access(getFolderPath(filePath), W_OK): 
        print(filePath,"no access")
        return False
    if path.isfile(filePath): 
        print(filePath,"not dir")
        return False
    return True