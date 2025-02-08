from .ai_enhancement import enhance_image

def compress_photo(file):
    try:
        output_path = "enhanced_photo.jpg"
        enhanced_image_path = enhance_image(file, output_path)
        return enhanced_image_path
    except Exception as e:
        print(f"Error: {e}")
        return None