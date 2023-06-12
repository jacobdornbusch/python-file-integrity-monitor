<h1>File Integrity Monitor (Proof of Concept)</h1>

This Python script monitors the integrity of files in a specified directory by calculating their hash values. It can be used to detect changes, modifications, and deletions of files in real-time.

<h2>How It Works</h2>

1. The script provides two options:

- Option A: Collect a new baseline of file hashes for the target files.
- Option B: Begin monitoring the files with a previously saved baseline.
2. If <b>Option A</b> is selected:

- The script calculates the SHA-512 hash for each file in the target directory.
- The file paths and their corresponding hashes are saved in a baseline file (baseline.txt by default).
3. If <b>Option B</b> is selected:

- The script loads the file paths and hashes from the baseline file.
- It continuously monitors the files for any changes, additions, or deletions.
4. During monitoring:

- For each file, the script recalculates the hash value and compares it to the saved baseline.
- If a new file is detected, it prints a notification indicating the file creation.
- If a file has been modified, it prints a notification indicating the change.
- If a file has been deleted, it prints a notification indicating the deletion.
5. The monitoring continues indefinitely until the script is interrupted or terminated.

<h2>How to Use</h2>

1. Clone the repository or download the script.

2. Place the target files in the Files directory.

3. Run the script using Python (Python 3.6 or later required).

4. Follow the prompts to collect a new baseline or begin monitoring.

5. The script will display notifications when changes, additions, or deletions occur.

<h2>Customization</h2>

- You can change the directory of the target files by modifying the script.
- The baseline file (baseline.txt) is stored in the same directory as the script by default, but you can customize the location by adjusting the file path in the code.
