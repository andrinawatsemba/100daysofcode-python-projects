import os


def batch_rename(folder_path, new_name):

    #soo this Renames all files in the folder to new_name_1, new_name_2, etc.
    try:
        # List all files in the folder
        files = os.listdir(folder_path)
        
        # Loop through files and rename
        for index, file in enumerate(files, start=1):
            # Get file extension
            file_ext = os.path.splitext(file)[1]
            
            # Create new file name
            new_file_name = f"{new_name}_{index}{file_ext}"
            
            # Get full paths
            old_file = os.path.join(folder_path, file)
            new_file = os.path.join(folder_path, new_file_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {file} → {new_file_name}")
        
        print("\n✅ All files renamed successfully!")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    folder = input("Enter folder path: ")
    name = input("Enter new base name: ")
    batch_rename(folder, name)
