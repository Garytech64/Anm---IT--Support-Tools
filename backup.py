import os
import shutil
import datetime

print("=== Multi-Folder Backup Script with Cleanup ===")

# Backup destination folder inside project root
backup_dir = os.path.join(os.getcwd(), "Backup")
os.makedirs(backup_dir, exist_ok=True)

# Timestamp for this backup
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Detect Desktop path (OneDrive or local)
user_profile = os.path.expanduser("~")
desktop_path = os.path.join(user_profile, "Desktop")
if not os.path.exists(desktop_path):
    desktop_path = os.path.join(user_profile, "OneDrive", "Desktop")

# Folders to back up
folders_to_backup = {
    "Desktop": desktop_path,
    "Documents": os.path.join(user_profile, "Documents"),
    "Downloads": os.path.join(user_profile, "Downloads")
}

def copy_folder(src, dest):
    """Copy folder contents while skipping protected files/folders."""
    try:
        for root, dirs, files in os.walk(src):
            rel_path = os.path.relpath(root, src)
            dest_path = os.path.join(dest, rel_path)
            os.makedirs(dest_path, exist_ok=True)
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_path, file)
                try:
                    shutil.copy2(src_file, dest_file)
                except PermissionError:
                    print(f"Skipped protected file: {src_file}")
    except Exception as e:
        print(f"Failed to copy {src}: {e}")

# Perform backup
for folder_name, source_path in folders_to_backup.items():
    if not os.path.exists(source_path):
        print(f"Warning: {folder_name} folder not found at {source_path}, skipping.")
        continue

    backup_path = os.path.join(backup_dir, f"{folder_name}_Backup_{timestamp}")
    copy_folder(source_path, backup_path)
    print(f"Backed up {folder_name} successfully: {backup_path}")

# Cleanup old backups older than 7 days
now = datetime.datetime.now()
for item in os.listdir(backup_dir):
    item_path = os.path.join(backup_dir, item)
    if os.path.isdir(item_path):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
        if (now - mtime).days > 7:
            try:
                shutil.rmtree(item_path)
                print(f"Deleted old backup: {item_path}")
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")
