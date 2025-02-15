#!/bin/bash
# start.sh

# Install system dependencies
apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0

# Install Python dependencies
pip install -r requirements.txt

# Jalankan aplikasi
gunicorn --bind 0.0.0.0:10000 wsgi:app