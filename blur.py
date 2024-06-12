import os
import subprocess

video_folder = "non violence part2"  # Replace with the actual path to your videos folder

for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        full_path = os.path.join(video_folder, filename)
        subprocess.call(["deface", full_path, "--thresh", "0.2"])