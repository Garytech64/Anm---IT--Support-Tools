import os
import shutil
import datetime

print("=== Backup Script ===")

# Example: backup Desktop to a folder called Backup inside ANM-IT-Support-Tools
source = os.path.expanduser("~/Desktop")
backup_dir = os.path.join(os.getcwd(), "Backup")

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_path = os.path.join(backup_dir, f"DesktopBackup_{timestamp}")

try:
    shutil.copytree(source, backup_path)
    print(f"Backup completed successfully: {backup_path}")
except Exception as e:
    print(f"Backup failed: {e}")
