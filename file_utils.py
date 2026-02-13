import os

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()

    image_ext = [".jpg", ".jpeg", ".png", ".gif"]
    video_ext = [".mp4", ".mkv", ".avi"]
    audio_ext = [".mp3", ".wav"]
    document_ext = [".pdf", ".docx", ".txt"]
    archive_ext = [".zip", ".rar"]
    program_ext = [".exe", ".msi"]

    if ext in image_ext:
        return "image"
    if ext in video_ext:
        return "video"
    if ext in audio_ext:
        return "audio"
    if ext in document_ext:
        return "document"
    if ext in archive_ext:
        return "archive"
    if ext in program_ext:
        return "program"

    return "other"
