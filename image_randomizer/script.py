import os
import random

def rename_and_randomize(start_num, end_num, collection_name, folder_path):

    while True:
        start_num = input("Starting Number: ")
        try:
            start_num = int(start_num)
            break
        except ValueError:
            print("Invalid input, please enter a number.")

    while True:
        end_num = input("Ending Number: ")
        try:
            end_num = int(end_num)
            if end_num <= start_num:
                print("Ending number must be greater than starting number.")
            else:
                break
        except ValueError:
            print("Invalid input, please enter a number.")

    while True:
        collection_name = input("Collection Name: ")
        if '/' in collection_name or '\\' in collection_name:
            print("Collection name cannot contain '/' or '\\'")
        else:
            break

    while True:
        folder_path = input("Folder path: ")
        if os.path.isdir(folder_path):
            break
        else:
            print("Invalid folder path, please enter a valid folder path.")


    total_files = len(os.listdir(folder_path))
    total_numbers = end_num - start_num + 1
    if total_files > total_numbers:
        print(f"There are more files ({total_files}) in the 'images' folder than possible random numbers between {start_num} and {end_num}.")
        return
    elif total_files < total_numbers:
        print(f"There are less files ({total_files}) in the 'images' folder than possible random numbers between {start_num} and {end_num}.")
        return
    else:
        print(f"total number of files: {total_files}")
        used_numbers = set()
        for file_name in os.listdir(folder_path):
            # Generate a random number between start_num and end_num
            new_num = random.randint(start_num, end_num)
            while new_num in used_numbers:
                new_num = random.randint(start_num, end_num)
            used_numbers.add(new_num)

            # Extract file extension
            _, file_ext = os.path.splitext(file_name)

            # Create new file name
            new_file_name = f"{collection_name} #{new_num}{file_ext}"

            # Rename the file
            os.rename(f"{folder_path}/{file_name}", f"{folder_path}/{new_file_name}")

rename_and_randomize()