# YouTube Video Downloader

This Python script allows you to download YouTube videos directly to your local machine using the `pytube` library. It is simple to use and handles all necessary configurations for downloading videos efficiently.

## Features
- Download videos in MP4 format.
- Automatically selects the first available progressive stream.
- Saves videos to a specified directory.

## Requirements
- Python 3.x
- `pytube` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. **Install the required libraries:**

    ```sh
    pip install pytube
    ```

3. **Ensure you have `dotenv` installed if you plan to use environment variables:**

    ```sh
    pip install python-dotenv
    ```

## Usage

1. **Run the script:**

    ```sh
    python downloader.py
    ```

2. **Input the URL of the YouTube video you wish to download when prompted.**

3. **The video will be downloaded to the specified directory (default is `C:/Users/Oxide-1/Downloads`).**

### Example

```sh
Enter the URL of the video to download: https://www.youtube.com/watch?v=example
Download completed successfully!
