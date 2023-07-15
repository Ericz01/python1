from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print('Title: ', yt.title)

print('Views: ', yt.views)

vid_download = yt.streams.get_highest_resolution()

vid_download.download()
