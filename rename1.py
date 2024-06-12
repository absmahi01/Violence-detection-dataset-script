import os

def rename_videos(folder_path, start_index=1001):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only video files
    video_files = [file for file in files if file.endswith(('.mp4', '.avi', '.mkv', '.mov'))]
    
    # Sort the video files
    video_files.sort()
    
    # Rename each video file
    for i, video_file in enumerate(video_files, start=start_index):
        # Generate the new name for the video file
        new_name = f"{i}" + os.path.splitext(video_file)[1]
        
        # Construct the old and new paths
        old_path = os.path.join(folder_path, video_file)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        print(f"Renamed {video_file} to {new_name}")

# Example usage
folder_path = 'NonViolence'
rename_videos(folder_path, start_index=1001)
