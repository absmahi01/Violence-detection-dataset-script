import filecmp
import os

def compare_folders(folder1, folder2):
    non_similar_files = []

    dcmp = filecmp.dircmp(folder1, folder2)

    # Check for files in the first directory not present in the second directory
    non_similar_files.extend([os.path.join(folder1, f) for f in dcmp.left_only])

    # Check for files in the second directory not present in the first directory
    non_similar_files.extend([os.path.join(folder2, f) for f in dcmp.right_only])

    # Recursively compare common subdirectories
    for sub_dir in dcmp.common_dirs:
        sub_folder1 = os.path.join(folder1, sub_dir)
        sub_folder2 = os.path.join(folder2, sub_dir)
        non_similar_files.extend(compare_folders(sub_folder1, sub_folder2))

    # Compare common files in both directories
    for common_file in dcmp.common_files:
        file1 = os.path.join(folder1, common_file)
        file2 = os.path.join(folder2, common_file)
        if not filecmp.cmp(file1, file2, shallow=False):
            non_similar_files.append(file1)
            non_similar_files.append(file2)

    return non_similar_files

if __name__ == "__main__":
    folder1 = input("Blurred_1")
    folder2 = input("Masked_1")

    non_similar_files = compare_folders(folder1, folder2)

    if non_similar_files:
        print("Non-similar files:")
        for file in non_similar_files:
            print(file)
    else:
        print("Folders contain exact same files.")
