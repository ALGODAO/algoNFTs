#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys

from lib.file_helper import get_files_in_folder
from lib.settings import Settings


def batch_add_parameter(config):
    """
    Adds a parameter to each NFT's .json file
    """
    files = get_files_in_folder(config.folder, "json")
    for file in files:
        if file.startswith("_metadata"):
            # we do not want to change the metadata file because we use the metadata file for each NFT
            continue
        with open(os.path.join(config.folder, file), "r") as f:
            json_data = json.load(f)
        json_data["attributes"].append({
            "trait_type": config.parameter_name,
            "value": config.parameter_value
        })
        with open(os.path.join(config.folder, file), "w") as f:
            json.dump(json_data, f, indent=2)


if __name__ == "__main__":
    settings = Settings("batch_add_parameter")

    batch_add_parameter(settings)

    print("Done.")
    sys.exit(0)
