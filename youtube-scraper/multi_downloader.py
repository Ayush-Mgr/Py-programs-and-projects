from pytubefix import YouTube
from pytubefix.cli import on_progress

list_url = ["https://www.youtube.com/watch?v=QP17MZp7yTg","https://www.youtube.com/watch?v=-wwEaTae1zw&pp=ygUGbXVzaWNz","https://www.youtube.com/watch?v=cl0a3i2wFcc&pp=ygUGbXVzaWNz","https://www.youtube.com/watch?v=AX6OrbgS8lI&pp=ygUGbXVzaWNz"]
for url in list_url:
  yt = YouTube(url, on_progress_callback = on_progress)
  print(yt.title)
  ys = yt.streams.get_audio_only()
  ys.download(output_path="/content/Downloads",mp3= True )
