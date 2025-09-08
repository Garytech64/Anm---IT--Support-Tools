import os
import shutil
import datetime

print("=== Multi-Folder Backup Script with Cleanup ===")

# Folders to back up
user_profile = os.environ["USERPROFILE"]
folders_to_backup = {
    "Desktop": os.path.join(user_profile, "OneDrive", "Desktop"),
    "Documents": os.path.join(user_profile, "Documents"),
    "Downloads": os.path.join(user_profile, "Downloads"),
}

backup_root = os.path.join(os.getcwd(), "Backup")
os.makedirs(backup_root, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

log_file = os.path.join(backup_root, "backup_log.txt")
success_count = 0
fail_count = 0
skipped_files = []


def log(message):
    """Write to console and append to log file"""
    print(message)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def ignore_files(dir, files):
    """Ignore .PST files and return them for logging"""
    global skipped_files
    ignored = [f for f in files if f.lower().endswith(".pst")]
    for f in ignored:
        skipped_files.append(os.path.join(dir, f))
    return ignored


for name, folder in folders_to_backup.items():
    if not os.path.exists(folder):
        log(f"Warning: {name} folder not found at {folder}, skipping.")
        fail_count += 1
        continue

    backup_path = os.path.join(backup_root, f"{name}_Backup_{timestamp}")
    try:
        shutil.copytree(folder, backup_path, ignore=ignore_files)
        log(f"Backed up {name} successfully: {backup_path}")
        success_count += 1
    except Exception as e:
        log(f"Failed to back up {name}: {e}")
        fail_count += 1


# Cleanup: keep only 3 most recent backups per folder
for folder_name in folders_to_backup.keys():
    backups = [d for d in os.listdir(backup_root) if d.startswith(folder_name)]
    backups.sort(reverse=True)
    for old in backups[3:]:
        old_path = os.path.join(backup_root, old)
        try:
            shutil.rmtree(old_path)
            log(f"Deleted old backup: {old}")
        except Exception as e:
            log(f"Could not delete {old}: {e}")

# Log skipped files
if skipped_files:
    log("\nSkipped locked/system files:")
    for f in skipped_files:
        log(f"  - {f}")

# Summary
summary = f"\nBackup finished: {success_count}/{len(folders_to_backup)} folders backed up successfully, {fail_count} failed, {len(skipped_files)} files skipped."
log(summary)
