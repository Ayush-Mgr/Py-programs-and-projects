# YouTube Downloader with Pytubefix

This program allows you to download multiple YouTube videos or convert them to MP3 format using Pytubefix.

## Getting Started with <a href="https://colab.research.google.com/">GOOGLE COLAB</a> file and follow the steps

To use this script, you'll need to run it in a Google Colab environment. Follow the steps below to set up and use the downloader:

### Step 1: Install the Required Libraries

First, install the necessary libraries by running the following command in a Colab cell:

<p align="center">
  <img src="https://github.com/Ayush-Mgr/Ayush-Mgr/blob/eeacf18200577946d7dc39feeb95ada0ad183236/assets/Screenshot%20from%202024-08-06%2010-05-26%20(2).png" width="50%" alt="Installation Command" />
</p>

<pre>
<code>
%pip install Pytubefix
</code>
</pre>

### Step 2: Run the Download Code

Next, use the provided code snippet to download videos or convert them to MP3 format. Paste the code into a new Colab cell and run it:

<pre>
<code>
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=QP17MZp7yTg"

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download(output_path="C:\\Users\\user\\Desktop\\tralpytube",mp3= True )
</code>
</pre>

Download multiple files:
<pre>
<code>

from pytubefix import YouTube
from pytubefix.cli import on_progress

list_url = ["https://www.youtube.com/watch?v=QP17MZp7yTg","https://www.youtube.com/watch?v=-wwEaTae1zw&pp=ygUGbXVzaWNz","https://www.youtube.com/watch?v=cl0a3i2wFcc&pp=ygUGbXVzaWNz","https://www.youtube.com/watch?v=AX6OrbgS8lI&pp=ygUGbXVzaWNz"]
for url in list_url:
  yt = YouTube(url, on_progress_callback = on_progress)
  print(yt.title)
  ys = yt.streams.get_audio_only()
  ys.download(output_path="/content/Downloads",mp3= True )
</code>
</pre>

## Notes

- Replace `url`or`list_url` with the URL of the YouTube video you want to download.
- Specify the `output_path` to define where the video should be saved.
- Remove `mp3 = True` to download file as VIDEO.

Feel free to modify the code to suit your needs and explore the capabilities of the Pytubefix library!

## Additional Resources

- <a href="https://pypi.org/project/pytubefix/" target="_blank">Pytubefix Documentation</a>

