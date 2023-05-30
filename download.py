# https://github.com/yt-dlp/yt-dlp#embedding-examples
# https://github.com/yt-dlp/yt-dlp#installation
# https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184

# todo create csv file to keep track of the video information
# tree
# channelName
    # csv
    # video folder
        # video file
        # audio file
        # other info folder


import yt_dlp

URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }],
    'writesubtitles': True,
    'writeautomaticsub': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)