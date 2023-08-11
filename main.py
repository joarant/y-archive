import download
import fileManagment
import csvManagment

# tee dict jossa id:t jotka tarvii kamaa esim vidin

def downloadVideo():
    fileManagment.clearTemp()
    load = download.downloadObj
    load.downloadData()
    load.download()
    fileManagment.clearTemp()

def downloadAudio():
    fileManagment.clearTemp()
    load = download.downloadObj
    load.downloadData()
    load.audioDownload()
    fileManagment.clearTemp()

def downloadData(urls, comments):
    fileManagment.clearTemp()
    load = download.downloadObj
    load.downloadData(urls, comments)
    fileManagment.clearTemp()


