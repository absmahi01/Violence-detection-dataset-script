import subprocess
import os

# Path to the detect.py script
detect_script = "detect.py"

# Path to the folder containing videos
video_folder = "G:\\Mahi\\yolov7-pose\\violence eshita blurred"

# Common arguments for all videos
common_args = "--weights yolov7-w6-pose.pt --kpt-label --hide-labels --hide-conf --line-thickness 8 --nobbox"

# Iterate through each video file in the folder
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        video_path = os.path.join(video_folder, filename)

        # Construct the full command for the current video
        command = f"python {detect_script} {common_args} --source \"{video_path}\""

        # Run the command using subprocess
        subprocess.call(command, shell=True)

print("Processing complete for all videos!")