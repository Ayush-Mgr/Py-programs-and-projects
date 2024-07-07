from pytube import YouTube
YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
yt.streamsfilter(progressive=True, file_extension='mp4')
try:
    yt.download()
except:
    print(f"failed {yt.title}")
print(f"done {yt.title}")


