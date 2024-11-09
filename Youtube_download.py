
from yt_dlp import YoutubeDL


def get_video_title(video_url):
    # Returning just the title of the video
    try:
        with YoutubeDL() as myVideo:
            info_dict = myVideo.extract_info(video_url, download=False)
            return info_dict.get("title", "No title found")
    except Exception as e:
        print("An error occurred while fetching the title:", e)
        return None


def download_video(video_url):
    # Options for yt-dlp
    ydl_opts = {
        'format': 'best',  # best available quality
        'outtmpl': '%(title)s.%(ext)s',  # Save file as the video's title
        'ffmpeg_location': "C:\\Users\\user\\OneDrive\\Documents\\ffmpeg-7.0.2-essentials_build\\bin"
    }

    try:
        with YoutubeDL(ydl_opts) as myDownload:
            print("Downloading...")
            myDownload.download([video_url])  # Download the video
            print("Download completed!")
    except Exception as e:
        print("An error occurred:", e)

def download_audio(video_url):
    #Downloading audio only from the URL
    # Options for yt-dlp to download audio only
    ydl_opts = {
        'format': 'bestaudio/best',  # highest quality audio
        'outtmpl': '%(title)s.%(ext)s',  # Save file as the audio's title
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract only audio
            'preferredcodec': 'mp3',      # Convert to mp3
            'preferredquality': '192',    # Set audio quality
        }],
        'ffmpeg_location': "C:\\Users\\user\\OneDrive\\Documents\\ffmpeg-7.0.2-essentials_build\\bin"
    }

    try:
        with YoutubeDL(ydl_opts) as myDownload:
            print("Downloading audio...")
            myDownload.download([video_url])  # Download the audio
            print("Audio download completed!")
    except Exception as e:
        print("An error occurred:", e)

video_url = input("Enter YouTube video link: ")

print(get_video_title(video_url))
download_audio(video_url)


