import os
import shutil
import datetime

print("=== Multi-Folder Backup Script with Cleanup ===")

folders_to_backup = ["Desktop", "Documents", "Downloads"]
days_to_keep = 7

user_profile = os.environ.get("USERPROFILE")
if not user_profile:
    print("Error: Cannot find USERPROFILE environment variable.")
    exit(1)

backup_dir = os.path.join(os.getcwd(), "Backup")
os.makedirs(backup_dir, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

for folder_name in folders_to_backup:
    source_path = os.path.join(user_profile, folder_name)
    if not os.path.exists(source_path):
        print(f"Warning: {folder_name} folder not found at {source_path}, skipping.")
        continue

    backup_path = os.path.join(backup_dir, f"{folder_name}_Backup_{timestamp}")
    try:
        shutil.copytree(source_path, backup_path)
        print(f"Backed up {folder_name} successfully: {backup_path}")
    except Exception as e:
        print(f"Failed to back up {folder_name}: {e}")

# Cleanup old backups
now = datetime.datetime.now()
for item in os.listdir(backup_dir):
    item_path = os.path.join(backup_dir, item)
    if os.path.isdir(item_path):
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
        if (now - mtime).days > days_to_keep:
            try:
                shutil.rmtree(item_path)
                print(f"Deleted old backup: {item_path}")
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")
