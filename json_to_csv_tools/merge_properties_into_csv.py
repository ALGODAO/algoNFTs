#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys

from lib.settings import Settings


def merge_properties_into_csv(config):
    """
    Reads and collects properties from .json files and merges them in a .csv file.
    Each csv row corresponds to the .json file with the same id.

    Make sure that all files from 1.json to n.json are present.
    """
    property_table = []
    for i in range(config.nft_count):
        property_table.append(read_properties_from_json(os.path.join(config.folder, str(i + 1) + '.json')))

    with open(os.path.join(config.folder, config.output_csv), 'w') as f:
        # The header row lists all properties
        header_row = ",".join(config.trait_types)
        f.write(header_row + "\n")

        # The rest of the rows contain the properties for each NFT
        for nft in property_table:
            row = ",".join([str(nft[trait_type]) for trait_type in config.trait_types])
            f.write(row + "\n")


def read_properties_from_json(file):
    """
    Reads properties from a json file.
    """
    properties = {}
    with open(file, 'r') as f:
        for prop in json.load(f)["attributes"]:
            properties[prop["trait_type"]] = prop["value"]
    return properties


if __name__ == "__main__":
    settings = Settings("merge_properties_into_csv")

    merge_properties_into_csv(settings)

    print("Done.")
    sys.exit(0)
