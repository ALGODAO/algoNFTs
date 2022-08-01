#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import sys

from lib.file_helper import get_files_in_folder
from lib.settings import Settings


def batch_id_shuffle(config):
    """
    Shuffle NFT ids in a folder including the image and json file.
    """
    folder = config.folder
    images = get_files_in_folder(folder, config.image_extension)
    ids = [int(image.split('.')[0]) for image in images]

    for _ in range(config.shuffle_times):
        # monkey shuffle by swapping two random ids
        id1 = ids[int(len(ids) * random.random())]
        id2 = ids[int(len(ids) * random.random())]
        if id1 == id2:
            continue

        for extension in [config.image_extension, config.metadata_extension]:
            file1 = str(id1) + '.' + extension
            file2 = str(id2) + '.' + extension
            temp_name = "temp_shuffle" + '.' + extension

            os.rename(os.path.join(folder, file1), os.path.join(folder, temp_name))
            os.rename(os.path.join(folder, file2), os.path.join(folder, file1))
            os.rename(os.path.join(folder, temp_name), os.path.join(folder, file2))

        print(f"Swapped {id1} and {id2}")


if __name__ == "__main__":
    settings = Settings("batch_id_shuffle")

    batch_id_shuffle(settings)

    print("Done.")
    sys.exit(0)
