# https://github.com/yt-dlp/yt-dlp#embedding-examples
# https://github.com/yt-dlp/yt-dlp#installation
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184

# todo create csv file to keep track of the video information

import csvManagment as cm
import os
import json
import yt_dlp
import fileManagment as fm


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
        def __init__(self, dObject):
                yt_dlp.postprocessor.PostProcessor.__init__(self)
                self.downloadObject = dObject

        def run(self, info):
            self._configuration_args()
            info["uploader"] = info["uploader"].replace("/", "⧸")
            info["title"] = info["title"].replace("/", "⧸")

            if "comments" in info:
                comments = {"comments": info["comments"]}
                with open(os.path.join("tempFileLocation",info["title"] + " ["+ info["id"]+"]" + 'comments.json'), 'w') as fp:
                    json.dump(comments, fp)
                fp.close()

            if fm.checkIfExsists(fm.getPath(info["uploader"])) == False: # uploader folder
                path = fm.createChannelFolder(info["uploader"],"")
                cm.createCsvFiles(path)

            if fm.checkIfExsists(fm.getPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]"))) == False: # video folder
                fm.createVideoFolder(info["title"] + " ["+ info["id"]+"]", fm.getFolderPath(info["uploader"]))

            fm.moveFiles(fm.getFolderPath("tempFileLocation"),
                          fm.getFolderPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]")))
            
            cm.updateChannelCsv(os.path.join(info["uploader"], "channelInfo.csv"),info)
            status = cm.updateVideoCsv(os.path.join(info["uploader"], "videoInfo.csv"),
                                       fm.getFolderPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]")))
            self.downloadObject.vidInfo[status["id"]] = status
            return [], info

class downloadObj:
    def __init__(self):
        self.vidInfo = {}


    def alreadyVideo(info, *, incomplete):
        info["uploader"] = info["uploader"].replace("/", "⧸")
        info["title"] = info["title"].replace("/", "⧸")
        if fm.checkIfExsists(fm.getPath(info["uploader"])) == True: # uploader folder
            if fm.checkIfExsists(fm.getPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]"))) == True: # video folder
                paths = cm.getPaths(fm.getPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]")))
                if len(paths["video_path"]) > 0:
                    return "video already downloaded"

    def alreadyAudio(info, *, incomplete):
        info["uploader"] = info["uploader"].replace("/", "⧸")
        info["title"] = info["title"].replace("/", "⧸")
        if fm.checkIfExsists(fm.getPath(info["uploader"])) == True: # uploader folder
            if fm.checkIfExsists(fm.getPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]"))) == True: # video folder
                paths = cm.getPaths(fm.getPath(os.path.join(info["uploader"], info["title"] + " ["+ info["id"]+"]")))
                if len(paths["audio_path"]) > 0:
                    return "audio already downloaded"

                
    def downloadData(self, urls, subtitles=False, thumbnail=False, getComments=False):
        ydl_opts = {
        'writesubtitles': subtitles,
        'writeautomaticsub': subtitles,
        "skip_download": True,
        "writeinfojson": True,
        "clean_infojson": True,
        "getcomments": getComments,
        "writethumbnail": thumbnail,
        "paths":{"home": "tempFileLocation"},
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(self), when='after_video')
            error_code = ydl.download(urls)

        return self.vidInfo

    def download(self, urls):
        ydl_opts = {
        "paths":{"home":"tempFileLocation"},
        'match_filter': downloadObj.alreadyVideo,
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
        'match_filter': downloadObj.alreadyAudio,
        "paths":{"home":"tempFileLocation"}
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.add_post_processor(MyCustomPP(self), when='after_video')
            error_code = ydl.download(urls)

