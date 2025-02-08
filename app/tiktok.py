from TikTokApi import TikTokApi

def download_tiktok_video(url):
    try:
        api = TikTokApi.get_instance()
        video = api.get_video_by_url(url)
        with open("tiktok_video.mp4", "wb") as f:
            f.write(video)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False