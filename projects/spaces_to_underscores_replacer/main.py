import os

# folder path
folder = r"C:\Users\Lenovo\Desktop\Python\lessons"

for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)
    if os.path.isfile(old_path):
        # space to underscore replacement
        new_filename = filename.replace(" ", "_")
        new_path = os.path.join(folder, new_filename)
        
        # Only rename if the filename is actually changing
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

print("✅ All files renamed successfully!")
