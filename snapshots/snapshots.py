import argparse
import csv
import os

def append():
    # Read in the holder-snapshot.csv file
    with open('holder-snapshot.csv', 'r') as holder:
        csv_reader = csv.DictReader(holder)
        holder_data = [row for row in csv_reader]

    # Make the holders data unique
    unique_holders = set()
    for row in holder_data:
        unique_holders.add(row['owner'])

    # Create an holder's array of dictionaries
    holder_data = []
    for owner in unique_holders:
        holder_data.append({'address': owner, 'max claimable': 1}) # max claim is customizable

    # Append the data to the wallets.csv
    with open('wallets.csv', 'a', newline='') as wallets:
        fieldnames = ['address', 'max claimable']
        writer = csv.DictWriter(wallets, fieldnames=fieldnames)
        if(wallets.tell() == 0):
            writer.writeheader()
        writer.writerows(holder_data)

def final():
    # Read in the wallets.csv file
    with open('wallets.csv', 'r') as wallets:
        csv_reader = csv.DictReader(wallets)
        wallet_data = [row for row in csv_reader]

    # Make the address data unique
    unique_addresses = set()
    for row in wallet_data:
        unique_addresses.add(row['address'])

    # Write the unique wallet addresses data back to the final.csv file
    with open('final.csv', 'w', newline='') as final:
        csv_writer = csv.DictWriter(final, fieldnames=['address', 'maxClaimable'])
        csv_writer.writeheader()
        for address in unique_addresses:
            csv_writer.writerow({'address': address, 'maxClaimable': 1})


def reset():
    try:
        os.remove("wallets.csv")
        os.remove("final.csv")
        print("Files 'wallets.csv' and 'final.csv' have been removed.")
    except FileNotFoundError:
        print("One or both of the files 'wallets.csv' and 'final.csv' do not exist.")

def main(param):
    if param == "append":
        append()
    elif param == "final":
        final()
    elif param == "reset":
        reset()
    else:
        print("Only 'append', 'final' and 'reset' are available.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("param", help="the parameter you want to pass", choices=["append", "final", "reset"])
    args = parser.parse_args()
    main(args.param)
