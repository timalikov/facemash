import os

# Set the directory path where the files are located
directory = "images"

# Loop through all the files in the directory
for filename in os.listdir(directory):
    # Check if the file has the desired extension (e.g., .png)
    if not filename.endswith(".jpg"):
        # Rename the file with the new extension (e.g., .jpg)
        new_filename = os.path.join(directory, os.path.splitext(filename)[0] + ".jpg")
        os.rename(os.path.join(directory, filename), new_filename)
        print(f"{filename} renamed to {os.path.basename(new_filename)}")
