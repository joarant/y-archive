import download
import fileManagment
import csvManagment


def getUrls(vDict, video, audio):
    urls = []
    for entry in vDict:
        if video == True and vDict[entry]["video"] == "":
            urls.append(vDict[entry]["url"])

        if audio == True and vDict[entry]["audio"] == "":
            urls.append(vDict[entry]["url"])

    return urls

def downloadVideo(urls, comments):
    fileManagment.clearTemp()
    load = download.downloadObj()
    videoDict = load.downloadData(urls, comments)
    filteredUrls = getUrls(videoDict, True, False)
    load.download(filteredUrls)
    fileManagment.clearTemp()

def downloadAudio(urls, comments):
    fileManagment.clearTemp()
    load = download.downloadObj()
    videoDict = load.downloadData(urls, comments)
    filteredUrls = getUrls(videoDict, False, True)
    load.audioDownload(filteredUrls)
    fileManagment.clearTemp()

def downloadData(urls, subtitles, thumbnail, comments):
    fileManagment.clearTemp()
    load = download.downloadObj()
    videoDict = load.downloadData(urls, subtitles, thumbnail, comments)
    fileManagment.clearTemp()


# URLS = ['https://www.youtube.com/channel/UC1xIkVRNvJBxo8biQy_6_lg']
# URLS = ['https://www.youtube.com/watch?v=bUJqe8PgAT8&list=PLHWoCotuxs61cuC0OQShmUoR0mP_8YXFx&index=8']
# URLS = ['https://www.youtube.com/watch?v=xYTPTylpeKI', "https://www.youtube.com/watch?v=mB4cNvUuGnI"]

URLS = ['https://www.youtube.com/watch?v=wJd4GAVaQDw'] # ongelma
# URLS = ['https://www.youtube.com/watch?v=mB4cNvUuGnI']


downloadData(URLS, True, False, False)
# downloadVideo(URLS, False)
# download.download(URLS)