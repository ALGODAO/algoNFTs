import os

def check_and_create_path(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))


def get_files_in_folder(folder, extension):
    """
    Get all files in a folder with a given extension.
    """
    files = []
    for file in os.listdir(folder):
        if file.endswith(extension):
            files.append(file)
    return files
