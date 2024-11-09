from pytube import YouTube

youtubelink = input("Put YouTube Link: ")

myvideo = YouTube(youtubelink)

mydownload = myvideo.streams.get_highest_resolution()
mydownload.download()
print("Video downloaded successfully! ")

# def yt_title(link):
#     yt = YouTube(link)
#     title = yt.title
#     return title
# print(yt_title(youtubelink))