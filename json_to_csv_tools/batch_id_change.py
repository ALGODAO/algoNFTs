#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from lib.settings import Settings


def batch_id_change(config):
    """
    Rename files to change the id number of an NFT and its property file.
    """
    for folder in config.folders:
        for extension in config.file_extensions:
            files = get_files_in_folder(folder, extension)
            for file in files:
                filename_id = file.split('.')[0]
                # skip file if the name is no number
                if not filename_id.isdigit():
                    continue
                new_id = int(filename_id) + config.offset_to_add
                new_file = str(new_id) + '.' + extension
                os.rename(os.path.join(folder, file), os.path.join(folder, new_file))
                print(f"Renamed {file} to {new_file}")


def get_files_in_folder(folder, extension):
    """
    Get all files in a folder with a given extension.
    """
    files = []
    for file in os.listdir(folder):
        if file.endswith(extension):
            files.append(file)
    return files


if __name__ == "__main__":
    settings = Settings("batch_id_change")

    batch_id_change(settings)

    print("Done.")
    sys.exit(0)
