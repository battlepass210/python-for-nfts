# Discord Image Extractor & Metadata Converter

A Python script to extract mainly image files from a Discord channel and convert the extracted images into a .csv file and a .json file with metadata.

**This script was initially designed for working with [thirdweb](https://thirdweb.com/) NFT smart contracts.**

## Requirements
- python 3.x
- argparse library
- csv library
- json library
- discord.py library
- urllib library

## Usage
### Extracting Images
1. Replace "REPLACE THIS WITH CHANNEL ID" with the Discord channel ID in the assets() function.
2. Replace "REPLACE THIS WITH DISCORD BOT TOKEN" with the Discord bot token in the assets() function.
3. Run the script with the command `python script.py assets`.

### Converting to Metadata
1. Run the script with the command `python script.py metadata`.
2. Provide the path to the .csv file generated in the previous step.
3. Provide the path to the desired .json file.
4. Provide a description for the metadata.

## Author
Author: [battlepass210](https://github.com/battlepass210)
