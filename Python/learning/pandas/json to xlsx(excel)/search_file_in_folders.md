To retrieve the folder name (directory name) where each `timestamps.json` file was found, you can modify the script to extract the immediate directory name from the full path of the file. Here’s how you can implement this:

```python
import os

# Define the root directory where you want to start searching
root_dir = '/path/to/your/root/directory'

# Function to recursively search for 'timestamps.json' files
def find_timestamp_json_files(directory):
    timestamp_files = []
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        # Check if 'timestamps.json' file exists in the current directory
        if 'timestamps.json' in files:
            # If found, get the immediate directory name (folder name)
            folder_name = os.path.basename(root)
            # Construct the full file path
            file_path = os.path.join(root, 'timestamps.json')
            # Append tuple of (folder_name, file_path) to the list
            timestamp_files.append((folder_name, file_path))
    return timestamp_files

# Call the function to find all 'timestamps.json' files under 'root_dir'
found_files = find_timestamp_json_files(root_dir)

# Print all found folder names and file paths
for folder_name, file_path in found_files:
    print(f"Found 'timestamps.json' in folder: {folder_name}")
    print(f"File path: {file_path}\n")
```

### Explanation:

1. **find_timestamp_json_files(directory)**:
   - This function now returns a list of tuples `(folder_name, file_path)`.
   - It uses `os.walk()` to recursively traverse through all directories and subdirectories starting from `directory`.
   - For each directory (`root`), it checks the list of files (`files`) to see if `timestamps.json` is present.
   - If found, it extracts the immediate directory name (folder name) using `os.path.basename(root)`.
   - It constructs the full file path using `os.path.join(root, 'timestamps.json')`.
   - It then appends `(folder_name, file_path)` tuple to the `timestamp_files` list.

2. **Printing found folder names and file paths**:
   - After calling `find_timestamp_json_files(root_dir)`, `found_files` contains tuples where each tuple consists of the folder name (`folder_name`) and the file path (`file_path`) where `timestamps.json` was found.
   - It then iterates through `found_files` and prints the folder name and file path for each occurrence found.

### Notes:
- This approach provides the immediate directory name (folder name) where each `timestamps.json` file was found.
- Adjust the root directory (`root_dir`) to the actual path where you want to start searching.
- This modification allows you to clearly associate each `timestamps.json` file with its containing folder, which can be useful for further processing or organizing your data based on folder context.