from .ai_enhancement import enhance_video

def compress_video(file):
    try:
        output_path = "enhanced_video.mp4"
        enhanced_video_path = enhance_video(file, output_path)
        return enhanced_video_path
    except Exception as e:
        print(f"Error: {e}")
        return None