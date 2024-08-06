from pytubefix import YouTube
from pytubefix.cli import on_progress

list_url = [ "https://www.youtube.com/watch?v=DmH6YPWhaDY&pp=ygUFbWVtZXM%3D",
    "https://www.youtube.com/watch?v=YkE3WuU1DT8&pp=ygULbWVtZXMgc2lnbWE%3D",
    "https://www.youtube.com/watch?v=RLJ7NnJ7Rpo&pp=ygULbWVtZXMgc2lnbWE%3D"]

for url in list_url:
  try:
    yt = YouTube(url, on_progress_callback = on_progress)
    ffilename = yt.title
    print(yt.title)
    ys = yt.streams.get_audio_only()
    ys.download(filename=ffilename,output_path="/content/Downloads",mp3= True )
  except Exception as e :
    print(f"failed : {ffilename},error: {e}")
    continue


