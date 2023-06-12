import os
import hashlib
import time

def calculate_file_hash(file_path):
    """Calculate the SHA-512 hash of a file"""
    hasher = hashlib.sha512()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def erase_baseline_if_already_exists():
    """Delete baseline.txt if it already exists"""
    if os.path.exists('baseline.txt'):
        os.remove('baseline.txt')

print()
print("What would you like to do?")
print()
print("    A) Collect new Baseline?")
print("    B) Begin monitoring files with saved Baseline?")
print()
response = input("Please enter 'A' or 'B': ").upper()
print()

if response == "A":
    # Delete baseline.txt if it already exists
    erase_baseline_if_already_exists()

    # Calculate Hash from the target files and store in baseline.txt
    # Collect all files in the target folder
    files = os.listdir('./Files')

    # For each file, calculate the hash, and write to baseline.txt
    with open('baseline.txt', 'w') as baseline_file:
        for file_name in files:
            file_path = os.path.join('./Files', file_name)
            file_hash = calculate_file_hash(file_path)
            baseline_file.write(f"{file_path}|{file_hash}\n")
    
elif response == "B":
    file_hash_dictionary = {}

    # Load file|hash from baseline.txt and store them in a dictionary
    with open('baseline.txt', 'r') as baseline_file:
        for line in baseline_file:
            file_path, file_hash = line.strip().split('|')
            file_hash_dictionary[file_path] = file_hash

    # Begin (continuously) monitoring files with saved Baseline
    while True:
        time.sleep(1)
        
        files = os.listdir('./Files')

        # For each file, calculate the hash
        for file_name in files:
            file_path = os.path.join('./Files', file_name)
            file_hash = calculate_file_hash(file_path)

            # Notify if a new file has been created
            if file_path not in file_hash_dictionary:
                print(f"{file_path} has been created!")

            # Notify if a file has been changed
            elif file_hash_dictionary[file_path] != file_hash:
                print(f"{file_path} has changed!")

        # Check for deleted files
        for file_path in file_hash_dictionary.copy():
            if not os.path.exists(file_path):
                print(f"{file_path} has been deleted!")
                del file_hash_dictionary[file_path]
