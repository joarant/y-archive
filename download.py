# https://github.com/yt-dlp/yt-dlp#embedding-examples
# https://github.com/yt-dlp/yt-dlp#installation
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184

# todo create csv file to keep track of the video information

import csvManagment as cm

import yt_dlp
import fileManagment as fm

class downloadObj:

    # id: {url, video: false, subtitles, thumbnail, audio}
    vidInfo = []

    class MyCustomPP(yt_dlp.postprocessor.PostProcessor): # koita vaihtaa funktioksi
        def run(self, info):
            self.to_screen('Moving files')

            if fm.checkIfExsists(fm.getPath(info["uploader"])) == False:
                print("ei olemassa 1")
                path = fm.createChannelFolder(info["uploader"],"")
                cm.createCsvFiles(path)

            if fm.checkIfExsists(fm.getPath(info["uploader"] + "/" + info["title"])) == False:
                print("ei olemassa 2")
                fm.createVideoFolder(info["title"], fm.getFolderPath(info["uploader"]), info["id"])
                fm.moveFiles(fm.getFolderPath("tempFileLocation"), fm.getFolderPath(fm.getPath(info["uploader"] + "/" + info["title"])))

            # cm.createCsvFiles(fm.getPath(info["uploader"]))
            # cm.updateChannelCsv(fm.getPath(info["uploader"]),info["id"],info)
            cm.updateVideoCsv(fm.getPath(info["uploader"]),info["id"],info)

            return [], info


    def downloadData(self, urls, getComments=False):
        ydl_opts = {
        # 'writesubtitles': True,
        # 'writeautomaticsub': True,
        "skip_download": True,
        "writeinfojson": True,
        "clean_infojson": True,
        "getcomments": getComments,
        # "writethumbnail": True,
        "writelink": True,
        "paths":{"home": "tempFileLocation"},
        }


        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(self.MyCustomPP(), when='after_video')
            error_code = ydl.download(urls)


    def download(self, urls):
        ydl_opts = {
        "skip_download": True,

        # 'writesubtitles': True,
        # 'writeautomaticsub': True,
        # "skip_download": True,
        # "writeinfojson": True,
        # "clean_infojson": True,
        # "getcomments": True,
        # # "writethumbnail": True,
        # "writelink": True,
        "paths":{"home":"tempFileLocation"}
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(urls)


    def audioDownload(self, urls):
        ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        # 'writesubtitles': True,
        # 'writeautomaticsub': True,
        # "writeinfojson": True,
        # "clean_infojson": True,
        # "getcomments": True,
        # "writelink": True,
        "paths":{"home":"tempFileLocation"}
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download(urls)

    # noDownload(['https://www.youtube.com/watch?v=BaW_jenozKc'])