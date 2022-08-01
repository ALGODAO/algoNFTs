# JSON to CSV tools
This folder has a couple script to help you prepare the batch mint process.
It assumes that you have NFT images and property `.json` files in a folder.
For example as they are produced by the HashLips Art Engine.

batch_mint would also support Hash lips metadata, but it makes sense to transform it to `.csv` anyway because it requires less work to change all the fields to how we want it (name, description, etc.).

This means that the `_metadata.json` is ignored here.

## Merge properties from json to csv
It merges the data together from property `.json` files for each NFT into a single `.csv` table. 

## Batch id change
Rename files to change the id number of an NFT and its property file.

Adjust the parameters in `settings.yaml` and then run the `batch_id_change.py` script. 

## Batch id shuffle
Randomly shuffles NFT ids of images and property files.
Please first move the `.json` and `.png` files into the same folder.

Adjust the parameters in `settings.yaml` and then run the `batch_id_shuffle.py` script. 
