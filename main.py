import download
import fileManagment
import csvManagment

# lataa tiedot ja myöhemmin vidi jos tarvitsee
# lataa vidi ja tee temp kansio sille
# hanki vidin json
# kato onko vidin kanavalla jo kansiota
# tee kansio ja csv
# uudelleen nimeä temp kansio
# anna json csv maangerille
# poimi jsonista tiedot
# päivitä csv

def downloadVideo():
    download.downloadData()
    download.download()

def downloadAudio():
    download.downloadData()
    download.audioDownload()

def downloadData(urls, comments):
    download.downloadData(urls, comments)


