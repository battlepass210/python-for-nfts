# Snapshots.py

This script is mainly used to process snapshotted CSV files (from https://tools.roland.xyz/snapshot) in order to extract unique data and write it to a new file and upload it to [thridweb](https://thirdweb.com/explore) deployed contracts.

**This script was initially designed for working with [thirdweb](https://thirdweb.com/) NFT smart contracts.**

## Requirements
- python 3.x
- csv module
- os module
- argparse module

## Features
1. `append`:  Reads in the `holder-snapshot.csv` file and appends the unique owner data to the `wallets.csv` file.
2. `final`: Reads in the `wallets.csv` file and writes the unique address data to the `final.csv` file.
3. `reset`: Removes the `wallets.csv` and `final.csv` files.

## Usage
The script is run on command line and takes one parameter: "append", "final" or "reset".

### Append
1. Run the script with the command python `python script.py append`.
2. The `append()` function reads in the holder-snapshot.csv file, makes the data unique, and appends it to the wallets.csv file. The max claimable is customizable.

### Final
1. Run the script with the command python `python script.py final`.
2. The `final()` function reads in the wallets.csv file, makes the data unique, and writes it to the final.csv file.

### Reset
1. Run the script with the command python `python script.py reset`.
2. The `reset()` function deletes the wallets.csv and final.csv files.
Please note that the script assumes that the files holder-snapshot.csv, wallets.csv and final.csv are located in the same directory as the script.

## Author
Author: [battlepass210](https://github.com/battlepass210)
