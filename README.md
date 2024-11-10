## YouTube Video Downloader with yt-dlp (README.md)

This Python script utilizes `yt-dlp` to download videos and extract audio from YouTube URLs.

**Features:**

  - **Get Video Title:** Retrieves the title of a YouTube video from its URL.
  - **Download Video:** Downloads a YouTube video in the best available quality.
  - **Download Audio:** Extracts audio from a YouTube video and saves it as an MP3 file in the highest quality available (up to 192kbps).

**Requirements:**

  * Python 3 (tested with 3.x)
  * `yt-dlp` library (installation instructions below)
  * `ffmpeg` (required for audio extraction and conversion)

**Installation:**

1.  **yt-dlp:**

      - You can install `yt-dlp` via pip yt-dlp on your terminal

2.  **ffmpeg:**

      - Download `ffmpeg` from the official website: [https://www.google.com/url?sa=E&source=gmail&q=https://ffmpeg.org/download.html)
      - Follow the installation instructions for your operating system.

**Instructions:**

1.  **Save the script:** Save the code as a Python file (e.g., `youtube_downloader.py`).

2.  **Replace ffmpeg path (optional):**

      - If `ffmpeg` is not in your system path, update the `ffmpeg_location` variable in the script with the actual path to the `ffmpeg` executable.

3.  **Run the script:**

      - Open a terminal or command prompt and navigate to the directory where you saved the script.
      - Run the script using `python youtube_downloader.py`.

4.  **Enter YouTube URL:**

      - The script will prompt you to enter a YouTube video URL.
      - Paste the URL and press Enter.

**Usage:**

The script will first retrieve the video title using `get_video_title`. Then, you can choose between downloading the entire video or extracting the audio:

  - **Download Video:**

      - The script will download the video in the best available quality using the `'format': 'best'` option.
      - The downloaded video will be saved with the video title and its extension (e.g., `My Video.mp4`).

  - **Download Audio:**

      - The script will extract the audio from the video using `FFmpegExtractAudio` postprocessor.
      - The extracted audio will be saved as an MP3 file with the video title and `.mp3` extension (e.g., `My Video.mp3`).
      - You can adjust the audio quality by modifying the `'preferredquality'` option in the `ydl_opts` dictionary.

**Disclaimer:**

  - Downloading copyrighted content without permission is illegal. Use this script responsibly and only download videos that you have the rights to access.
  - YouTube may change their website structure or API, potentially affecting the script's functionality.

**Additional Notes:**

  - The script utilizes exception handling to gracefully handle potential errors during download.
  - The `outtmpl` option specifies the naming convention for downloaded files.
