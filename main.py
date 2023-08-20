import download
import fileManagment


def getUrls(vDict, video, audio):
    urls = []
    for entry in vDict:
        if video == True and vDict[entry]["video"] == "":
            urls.append(vDict[entry]["url"])

        if audio == True and vDict[entry]["audio"] == "":
            urls.append(vDict[entry]["url"])

    return urls

def downloadVideo(urls, subtitles, thumbnail, comments):
    fileManagment.clearTemp()
    load = download.downloadObj()
    # videoDict = load.downloadData(urls, subtitles, thumbnail, comments)
    # filteredUrls = getUrls(videoDict, True, False)
    # if len(filteredUrls) > 0:
    load.audioDownload(urls)
    fileManagment.clearTemp()

def downloadAudio(urls, subtitles, thumbnail, comments):
    fileManagment.clearTemp()
    load = download.downloadObj()
    # videoDict = load.downloadData(urls, subtitles, thumbnail, comments)
    # filteredUrls = getUrls(videoDict, False, True)
    # if len(filteredUrls) > 0:
    load.audioDownload(urls)
    fileManagment.clearTemp()

def downloadData(urls, subtitles, thumbnail, comments):
    fileManagment.clearTemp()
    load = download.downloadObj()
    load.downloadData(urls, subtitles, thumbnail, comments)
    fileManagment.clearTemp()


URLS = []


# downloadData(URLS, True, False, False)
# downloadVideo(URLS, True, True, True)
# downloadAudio(URLS, True, True, True)

