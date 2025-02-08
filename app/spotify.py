import spotdl

def download_spotify_audio(url):
    try:
        spotdl.download(url)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False