from pytube import YouTube

def video_info(video_url):
    yt = YouTube(video_url)
    title = yt.title
    views = yt.views
    return f"Title: {title}\n\nViews: {views}"

video_url = 'https://www.youtube.com/watch?v=2lAe1cqCOXo'

video_info(video_url)
