# Snapshots.py

This script is mainly used to process snapshotted CSV files (from https://tools.roland.xyz/snapshot) in order to extract unique data and write it to a new file and upload it to thridweb deployed contracts (https://thirdweb.com/explore). 

The script has 3 main functions:
- `append()`: Appends the unique data from the holder-snapshot.csv file to the wallets.csv file.
- `final()`: Extracts the unique data from the wallets.csv file and writes it to the final.csv file.
- `reset()`: Deletes the wallets.csv and final.csv files.

## Requirements
* python 3.x
* csv module
* os module
* argparse module

## Usage
The script is run on command line and takes one parameter: "append", "final" or "reset".

### Append
The `append()` function reads in the holder-snapshot.csv file, makes the data unique, and appends it to the wallets.csv file. The max claimable is customizable.

### Final
The `final()` function reads in the wallets.csv file, makes the data unique, and writes it to the final.csv file.

### Reset
The `reset()` function deletes the wallets.csv and final.csv files.
Please note that the script assumes that the files holder-snapshot.csv, wallets.csv and final.csv are located in the same directory as the script.

