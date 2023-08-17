# https://github.com/yt-dlp/yt-dlp#embedding-examples
# https://github.com/yt-dlp/yt-dlp#installation
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184

# todo create csv file to keep track of the video information

import csvManagment as cm
import weakref

import yt_dlp
import fileManagment as fm


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
        def __init__(self, dObject):
                yt_dlp.postprocessor.PostProcessor.__init__(self)
                self.downloadObject = dObject

        def run(self, info):
            self.to_screen('Moving files')
            print(self.downloadObject, "vidInfo")
            if fm.checkIfExsists(fm.getPath(info["uploader"])) == False: # uploader folder
                path = fm.createChannelFolder(info["uploader"],"")
                cm.createCsvFiles(path)

            if fm.checkIfExsists(fm.getPath(info["uploader"] + "/" + info["title"])) == False: # video folder
                fm.createVideoFolder(info["title"], fm.getFolderPath(info["uploader"]), info["id"])

            fm.moveFiles(fm.getFolderPath("tempFileLocation"), fm.getFolderPath(fm.getPath(info["uploader"] + "/" + info["title"])))
            # cm.updateChannelCsv(fm.getPath(info["uploader"]),info["id"],info)
            status = cm.updateVideoCsv(fm.getPath(info["uploader"]),info["id"],info)
            self.downloadObject.vidInfo[status["id"]] = status

            # self.downloadObject = None
            return [], info

class downloadObj:

    def __init__(self):
        self.vidInfo = {}

    def downloadData(self, urls, subtitles=False, thumbnail=False, getComments=False):
        ydl_opts = {
        'writesubtitles': subtitles,
        'writeautomaticsub': subtitles,
        "skip_download": True,
        "writeinfojson": True,
        "clean_infojson": True,
        "getcomments": getComments,
        "writethumbnail": thumbnail,
        # "writelink": True,
        "paths":{"home": "tempFileLocation"},
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(self), when='after_video')
            error_code = ydl.download(urls)

        return self.vidInfo

    def download(self, urls):
        ydl_opts = {
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
            ydl.add_post_processor(MyCustomPP(self), when='after_video')
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
            ydl.add_post_processor(MyCustomPP(self), when='after_video')
            error_code = ydl.download(urls)

    # noDownload(['https://www.youtube.com/watch?v=BaW_jenozKc'])