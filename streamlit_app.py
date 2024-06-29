import streamlit as st
import time
import gzip
import lzma
import io

# Function to handle file compression
def compress_file(file_data, algorithm):
    if algorithm == "gzip":
        return gzip.compress(file_data)
    elif algorithm == "lzma":
        return lzma.compress(file_data)
    else:
        raise ValueError("Unknown compression algorithm.")

# Function to handle file decompression
def decompress_file(file_data, algorithm):
    if algorithm == "gzip":
        return gzip.decompress(file_data)
    elif algorithm == "lzma":
        return lzma.decompress(file_data)
    else:
        raise ValueError("Unknown decompression algorithm.")

st.title("Compression Algorithm Comparison")

task = st.sidebar.selectbox("Choose Task:", ["Audio Compression", "Audio Decompression", "Image Compression", "Image Decompression", "Video Compression", "Video Decompression"])

# Audio Compression
if task == "Audio Compression":
    audio_file = st.file_uploader("Upload Audio File", type=["mp3", "wav", "ogg"])
    if audio_file:
        st.audio(audio_file, format=audio_file.type)
    algorithm = st.selectbox("Choose Compression Algorithm:", ["gzip", "lzma"])
    if audio_file and st.button("Compress Audio"):
        audio_data = audio_file.read()
        start_time = time.time()
        compressed_audio_data = compress_file(audio_data, algorithm)
        elapsed_time = time.time() - start_time
        st.success(f"Audio Compressed Successfully, Time Elapsed: {elapsed_time:.2f} seconds, Size: {len(compressed_audio_data) / 1024:.2f} KB")
        st.download_button("Download Compressed Audio", compressed_audio_data, "compressed_audio.bin")

# Audio Decompression
elif task == "Audio Decompression":
    compressed_audio_file = st.file_uploader("Upload Compressed Audio File", type=["bin"])
    algorithm = st.selectbox("Choose Decompression Algorithm:", ["gzip", "lzma"])
    if compressed_audio_file and st.button("Decompress Audio"):
        compressed_audio_data = compressed_audio_file.read()
        start_time = time.time()
        decompressed_audio_data = decompress_file(compressed_audio_data, algorithm)
        elapsed_time = time.time() - start_time
        st.success(f"Audio Decompressed Successfully, Time Elapsed: {elapsed_time:.2f} seconds, Size: {len(decompressed_audio_data) / 1024:.2f} KB")
        st.audio(io.BytesIO(decompressed_audio_data), format="audio/wav")
        st.download_button("Download Decompressed Audio", decompressed_audio_data, "decompressed_audio.wav")

# Image Compression
elif task == "Image Compression":
    image_file = st.file_uploader("Upload Image File", type=["jpg", "png", "bmp"])
    if image_file:
        st.image(image_file)
    algorithm = st.selectbox("Choose Compression Algorithm:", ["gzip", "lzma"])
    if image_file and st.button("Compress Image"):
        image_data = image_file.read()
        start_time = time.time()
        compressed_image_data = compress_file(image_data, algorithm)
        elapsed_time = time.time() - start_time
        st.success(f"Image Compressed Successfully, Time Elapsed: {elapsed_time:.2f} seconds, Size: {len(compressed_image_data) / 1024:.2f} KB")
        st.download_button("Download Compressed Image", compressed_image_data, "compressed_image.bin")

# Image Decompression
elif task == "Image Decompression":
    compressed_image_file = st.file_uploader("Upload Compressed Image File", type=["bin"])
    algorithm = st.selectbox("Choose Decompression Algorithm:", ["gzip", "lzma"])
    if compressed_image_file and st.button("Decompress Image"):
        compressed_image_data = compressed_image_file.read()
        start_time = time.time()
        decompressed_image_data = decompress_file(compressed_image_data, algorithm)
        elapsed_time = time.time() - start_time
        st.success(f"Image Decompressed Successfully, Time Elapsed: {elapsed_time:.2f} seconds, Size: {len(decompressed_image_data) / 1024:.2f} KB")
        st.image(io.BytesIO(decompressed_image_data))
        st.download_button("Download Decompressed Image", decompressed_image_data, "decompressed_image.jpg")

# Video Compression
elif task == "Video Compression":
    video_file = st.file_uploader("Upload Video File", type=["mp4", "avi", "mov"])
    if video_file:
        st.video(video_file)
    algorithm = st.selectbox("Choose Compression Algorithm:", ["gzip", "lzma"])
    if video_file and st.button("Compress Video"):
        video_data = video_file.read()
        start_time = time.time()
        compressed_video_data = compress_file(video_data, algorithm)
        elapsed_time = time.time() - start_time
        st.success(f"Video Compressed Successfully, Time Elapsed: {elapsed_time:.2f} seconds, Size: {len(compressed_video_data) / 1024:.2f} KB")
        st.download_button("Download Compressed Video", compressed_video_data, "compressed_video.bin")

# Video Decompression
elif task == "Video Decompression":
    compressed_video_file = st.file_uploader("Upload Compressed Video File", type=["bin"])
    algorithm = st.selectbox("Choose Decompression Algorithm:", ["gzip", "lzma"])
    if compressed_video_file and st.button("Decompress Video"):
        compressed_video_data = compressed_video_file.read()
        start_time = time.time()
        decompressed_video_data = decompress_file(compressed_video_data, algorithm)
        elapsed_time = time.time() - start_time
        st.success(f"Video Decompressed Successfully, Time Elapsed: {elapsed_time:.2f} seconds, Size: {len(decompressed_video_data) / 1024:.2f} KB")
        st.video(io.BytesIO(decompressed_video_data))
        st.download_button("Download Decompressed Video", decompressed_video_data, "decompressed_video.mp4")
