import cv2
import torch
from torchvision.transforms import ToTensor, ToPILImage
from PIL import Image

# Load pre-trained ESRGAN model (contoh sederhana)
def load_esrgan_model():
    # Anda bisa menggunakan model ESRGAN yang sudah dilatih
    # Contoh: https://github.com/xinntao/ESRGAN
    model = torch.hub.load('xinntao/ESRGAN', 'esrgan', pretrained=True)
    return model

def enhance_image(image_path, output_path):
    # Load model
    model = load_esrgan_model()

    # Buka gambar
    img = Image.open(image_path).convert('RGB')
    img_tensor = ToTensor()(img).unsqueeze(0)

    # Proses peningkatan kualitas
    with torch.no_grad():
        enhanced_tensor = model(img_tensor)

    # Simpan gambar yang sudah ditingkatkan
    enhanced_img = ToPILImage()(enhanced_tensor.squeeze(0))
    enhanced_img.save(output_path)
    return output_path

def enhance_video(video_path, output_path):
    # Buka video
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Buat video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Proses setiap frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Contoh: Tingkatkan kualitas frame menggunakan AI (misalnya, ESRGAN)
        enhanced_frame = cv2.detailEnhance(frame, sigma_s=10, sigma_r=0.15)
        out.write(enhanced_frame)

    # Release resources
    cap.release()
    out.release()
    return output_path