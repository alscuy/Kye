from flask import Blueprint, render_template, request, redirect, url_for, flash
from .youtube import download_youtube_video
from .tiktok import download_tiktok_video
from .spotify import download_spotify_audio
from .video_compressor import compress_video
from .photo_compressor import compress_photo
from .instagram_story import stalk_instagram_story
from .tiktok_profile import stalk_tiktok_profile

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('base.html')

@main_routes.route('/youtube', methods=['GET', 'POST'])
def youtube():
    if request.method == 'POST':
        url = request.form['url']
        quality = request.form['quality']  # Ambil kualitas dari form
        enhanced_video_path, error = download_youtube_video(url, quality)

        if error:
            flash(f"Error: {error}", 'danger')
        else:
            flash(f"Video berhasil diunduh dan ditingkatkan: {enhanced_video_path}", 'success')
        return redirect(url_for('main.youtube'))

    return render_template('youtube.html')
@main_routes.route('/tiktok', methods=['GET', 'POST'])
def tiktok():
    if request.method == 'POST':
        url = request.form['url']
        download_tiktok_video(url)
        flash('Video downloaded successfully!', 'success')
        return redirect(url_for('main.tiktok'))
    return render_template('tiktok.html')

@main_routes.route('/spotify', methods=['GET', 'POST'])
def spotify():
    if request.method == 'POST':
        url = request.form['url']
        download_spotify_audio(url)
        flash('Audio downloaded successfully!', 'success')
        return redirect(url_for('main.spotify'))
    return render_template('spotify.html')

@main_routes.route('/video_compressor', methods=['GET', 'POST'])
def video_compressor():
    if request.method == 'POST':
        file = request.files['file']
        compress_video(file)
        flash('Video compressed successfully!', 'success')
        return redirect(url_for('main.video_compressor'))
    return render_template('video_compressor.html')

@main_routes.route('/photo_compressor', methods=['GET', 'POST'])
def photo_compressor():
    if request.method == 'POST':
        file = request.files['file']
        compress_photo(file)
        flash('Photo compressed successfully!', 'success')
        return redirect(url_for('main.photo_compressor'))
    return render_template('photo_compressor.html')

@main_routes.route('/instagram_story', methods=['GET', 'POST'])
def instagram_story():
    if request.method == 'POST':
        username = request.form['username']
        stalk_instagram_story(username)
        flash('Stories fetched successfully!', 'success')
        return redirect(url_for('main.instagram_story'))
    return render_template('instagram_story.html')

@main_routes.route('/tiktok_profile', methods=['GET', 'POST'])
def tiktok_profile():
    if request.method == 'POST':
        username = request.form['username']
        stalk_tiktok_profile(username)
        flash('Profile fetched successfully!', 'success')
        return redirect(url_for('main.tiktok_profile'))
    return render_template('tiktok_profile.html')