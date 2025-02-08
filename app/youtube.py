from pytube import YouTube
from .ai_enhancement import enhance_video

def download_youtube_video(url, quality):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')

        # Pilih stream berdasarkan kualitas
        if quality == '360p':
            stream = streams.get_by_resolution('360p')
        elif quality == '480p':
            stream = streams.get_by_resolution('480p')
        elif quality == '720p':
            stream = streams.get_by_resolution('720p')
        elif quality == '1080p':
            stream = streams.get_by_resolution('1080p')
        else:
            stream = streams.get_highest_resolution()

        if not stream:
            return None, "Kualitas yang diminta tidak tersedia."

        # Download video
        video_path = stream.download(filename="temp_video.mp4")

        # Enhance video menggunakan AI
        enhanced_video_path = f"enhanced_{quality}_video.mp4"
        enhance_video(video_path, enhanced_video_path)

        return enhanced_video_path, None
    except Exception as e:
        return None, str(e)