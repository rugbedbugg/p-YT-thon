from dotenv import load_dotenv
import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError

link = input("Enter the URL of the video to download: ")
download_folder = os.getenv("PATH")

try:
    yt = YouTube(link)
    stream = yt.streams.first()
    stream.download(download_folder)
    print("Download completed successfully!")

except RegexMatchError:
    print("Invalid URL. Please check the URL and try again.")
except VideoUnavailable:
    print("Video unavailable. Please check if the video is accessible.")
except PytubeError as e:
    print(f"A Pytube error occurred: {e}")
except Exception as e:
    print(f"{e}")
