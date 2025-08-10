import os
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source exists
    if not os.path.exists(source_dir):
        print(f"❌ Error: Source directory '{source_dir}' does not exist.")
        return

    # Check if destination exists
    if not os.path.exists(dest_dir):
        print(f"❌ Error: Destination directory '{dest_dir}' does not exist.")
        return

    # Identify file types to be transferred
    file_types = set()
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            _, ext = os.path.splitext(filename)
            file_types.add(ext if ext else "No Extension")

    print("\n📂 File types to be transferred:")
    for ftype in file_types:
        print(f" - {ftype}")

    confirm = input("\nDo you want to continue with the backup? (y/n): ").strip().lower()
    if confirm != "y":
        print("Backup cancelled.")
        return

    try:
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)

            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, filename)

                # If file already exists, append timestamp
                if os.path.exists(dest_file):
                    name, ext = os.path.splitext(filename)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{name}_{timestamp}{ext}"
                    dest_file = os.path.join(dest_dir, new_filename)

                shutil.copy2(source_file, dest_file)
                print(f"✅ Copied: {filename}")

        print("\nBackup completed successfully!")

    except Exception as e:
        print(f"⚠️ Error during backup: {e}")


if __name__ == "__main__":
    source = input("Enter source directory path: ").strip()
    destination = input("Enter destination directory path: ").strip()
    backup_files(source, destination)
