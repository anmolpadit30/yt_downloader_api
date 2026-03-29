from pytubefix import YouTube
import os

def download_song_pytube(url):
    try:
        yt = YouTube(url, use_po_token=True)
        # Filter for audio only and select the first available stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        print(f"Downloading: {yt.title}")

        # Download the file (initially often webm or aac format)
        out_file = audio_stream.download()

        # Rename the file to .mp3 (assuming ffmpeg handles the underlying format)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(f"Successfully downloaded '{yt.title}' as MP3.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
video_url = input("Enter YouTube video URL: ").strip()

download_song_pytube(video_url)
