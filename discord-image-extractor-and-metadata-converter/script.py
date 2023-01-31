import argparse
import csv
import json
import discord
from urllib.parse import urlparse

def assets():
    csv_header = ['name', 'description', 'image']
    csv_data = []
    wrong_sorted_numbering = []
    correct_sorted_numbering_index = []
    final_csv_data = []


    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel('REPLACE THIS WITH CHANNEL ID')
        async for message in channel.history(limit=10000):
            if message.attachments:
                for attachment in message.attachments:
                    if attachment.height:
                        csv_data.append(["","",attachment.url])
        await client.close()

                    
    client.run('REPLACE THIS WITH DISCORD BOT TOKEN')

    csv_data = sorted(csv_data, key=lambda x: x[2].split("/")[-1]) # sort the data based on the image name

    for data in csv_data:
        image_name = data[2].split("/")[-1]
        last_part = image_name.split("_")[-1].split(".")[0]
        if last_part.isdigit():
            wrong_sorted_numbering.append(int(last_part))
        else:
            wrong_sorted_numbering.append(last_part)

    correct_sorted_numbering = sorted(wrong_sorted_numbering)
    print(correct_sorted_numbering)
    for i in correct_sorted_numbering:
        correct_sorted_numbering_index.append(wrong_sorted_numbering.index(i))

    for j in correct_sorted_numbering_index:
        final_csv_data.append(csv_data[j])

    with open('discord.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(csv_header)
        # write the data
        for data in final_csv_data:
            writer.writerow(data)    

def metadata():
    data = []
    csv_file = input("CSV file path: ")
    while not csv_file.endswith('.csv'):
        print("Error: only .csv files are accepted.")
        csv_file = input("CSV file path: ")

    json_file = input("JSON file path: ")
    while not json_file.endswith('.json'):
        print("Error: only .json files are accepted.")
        json_file = input("JSON file path: ")

    description = input("Descriptions for JSON Metadata: ")
    while not description and (description.isspace() or description == ""):
        user_input = input("Are you sure you want the description to be blank? (y/n) ").strip().lower()
        if user_input in ['y', 'yes']:
            description = ""
            break
    else:
        description = input("Descriptions for JSON Metadata: ")

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = urlparse(row["image"]).path.split("/")[-1].split(".")[0]
            if name.split("_")[-1].isdigit():
                name = name.rsplit("_", 1)[0] + " #" + name.rsplit("_", 1)[1]
            name = name.replace("_", " ")
            attribute = {key:value for key, value in row.items() if key not in ["name", "description", "image"]}
            if description:
                data.append({"name": name, "description": description, "image": row["image"], "attribute": attribute})
            else:
                data.append({"name": name, "description": row["description"], "image": row["image"], "attribute": attribute})

    with open(json_file, 'w') as f:
        json.dump(data, f)



def main(param):
    if param == "assets":
        assets()
    elif param == "metadata":
        metadata()
    else:
        print("Only 'assets' and 'metadata' are available.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("param", help="the parameter you want to pass", choices=["assets", "metadata"])
    args = parser.parse_args()
    main(args.param)