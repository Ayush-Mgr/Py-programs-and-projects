from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=QP17MZp7yTg"

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download(output_path="C:\\Users\\user\\Desktop\\tralpytube",mp3= True )
