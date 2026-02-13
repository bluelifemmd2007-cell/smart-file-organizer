import os
import json
import shutil
from utils.file_utils import get_file_type   # اینجا از پوشهٔ utils ایمپورت می‌کنی

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def organize_files():
    config = load_config()
    target_path = config["target_path"]
    rules = config["rules"]

    for file in os.listdir(target_path):
        file_path = os.path.join(target_path, file)

        if os.path.isfile(file_path):
            file_type = get_file_type(file)
            folder_name = rules.get(file_type, "Others")
            folder_path = os.path.join(target_path, folder_name)

            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))

            print(f"Moved: {file} → {folder_name}")

if __name__ == "__main__":
    organize_files()
