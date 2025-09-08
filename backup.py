import os
import shutil
import datetime

# === Multi-Folder Backup Script with Logging and Cleanup ===

# Define folders to back up
user_profile = os.environ["USERPROFILE"]
folders_to_backup = {
    "Desktop": os.path.join(user_profile, "OneDrive", "Desktop"),
    "Documents": os.path.join(user_profile, "Documents"),
    "Downloads": os.path.join(user_profile, "Downloads"),
}

# Backup root
backup_root = os.path.join("C:\\ANM-IT-Support-Tools", "Backup")
os.makedirs(backup_root, exist_ok=True)

# Log file
log_file = os.path.join(backup_root, "backup_log.txt")
with open(log_file, "w") as f:
    f.write("=== Backup Log ===\n")
    f.write(f"Run at: {datetime.datetime.now()}\n\n")

print("=== Multi-Folder Backup Script with Cleanup ===")

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
all_success = True

for label, src in folders_to_backup.items():
    if not os.path.exists(src):
        print(f"Warning: {label} folder not found at {src}, skipping.")
        with open(log_file, "a") as f:
            f.write(f"Warning: {label} folder not found at {src}, skipping.\n")
        continue

    dst = os.path.join(backup_root, f"{label}_Backup_{timestamp}")

    try:
        shutil.copytree(src, dst)
        print(f"Backed up {label} successfully: {dst}")
        with open(log_file, "a") as f:
            f.write(f"Backed up {label} successfully: {dst}\n")
    except shutil.Error as e:
        print(f"Failed to back up {label}: {e.args}")
        with open(log_file, "a") as f:
            f.write(f"Failed to back up {label}: {e.args}\n")
        all_success = False
    except (PermissionError, OSError) as e:
        print(f"Skipped file(s) in {label}: {e}")
        with open(log_file, "a") as f:
            f.write(f"Skipped file(s) in {label}: {e}\n")
        all_success = False

# Cleanup old backups (keep latest 3 per folder)
for label in folders_to_backup.keys():
    backups = [d for d in os.listdir(backup_root) if d.startswith(label + "_Backup_")]
    backups.sort(reverse=True)
    for old in backups[3:]:
        try:
            shutil.rmtree(os.path.join(backup_root, old))
            print(f"Deleted old backup: {old}")
            with open(log_file, "a") as f:
                f.write(f"Deleted old backup: {old}\n")
        except Exception as e:
            print(f"Could not delete {old}: {e}")
            with open(log_file, "a") as f:
                f.write(f"Could not delete {old}: {e}\n")

if all_success:
    print("Multi-Folder Backup completed successfully.")
    with open(log_file, "a") as f:
        f.write("Multi-Folder Backup completed successfully.\n")
else:
    print("Multi-Folder Backup completed with errors. See backup_log.txt for details.")
    with open(log_file, "a") as f:
        f.write("Multi-Folder Backup completed with errors.\n")
