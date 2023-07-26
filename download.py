# https://github.com/yt-dlp/yt-dlp#embedding-examples
# https://github.com/yt-dlp/yt-dlp#installation
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184

# todo create csv file to keep track of the video information

import random
import string
import os
import csvManagment as cm

import yt_dlp
import fileManagment as fm


def my_hook(d):
    print()
    print()
    print(d)
    print()
    print()

    # if d['status'] == 'finished':
    #     print()
    #     print(d['filename'])
    #     print("---------------------")

        # nappaa id ja uudelleen nimeä kansiot

# def get_random_string():
#     length = 8
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     print("Random string of length", length, "is:", )
#     os.mkdir(result_str)
#     return result_str

# POSTPROCESS_WHEN = ('pre_process', 'after_filter', 'video', 'before_dl', 'post_process', 'after_move', 'after_video', 'playlist')

class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
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
        cm.updateCsv(fm.getPath(info["uploader"]),info["id"],info)

        return [], info


def downloadData(urls, getComments=False):
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
        ydl.add_post_processor(MyCustomPP(), when='after_video')
        error_code = ydl.download(urls)
    


def download(urls):
    ydl_opts = {
    # 'writesubtitles': True,
    # 'writeautomaticsub': True,
    # "skip_download": True,
    # "writeinfojson": True,
    # "clean_infojson": True,
    # "getcomments": True,
    # # "writethumbnail": True,
    # "writelink": True,
    "paths":{"home":"moi"}
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)


def audioDownload(urls):
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
    "paths":{"home":"moi"}
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)

# noDownload(['https://www.youtube.com/watch?v=BaW_jenozKc'])