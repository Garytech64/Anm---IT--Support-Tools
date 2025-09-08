import os
import shutil
import datetime

print("=== Multi-Folder Backup Script with Cleanup ===")

# Paths to back up
folders_to_backup = {
    "Desktop": os.path.expanduser("~/OneDrive/Desktop"),
    "Documents": os.path.expanduser("~/Documents"),
    "Downloads": os.path.expanduser("~/Downloads")
}

backup_root = os.path.join(os.getcwd(), "Backup")
if not os.path.exists(backup_root):
    os.makedirs(backup_root)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
summary = {"success": 0, "failed": 0, "skipped_files": []}

log_file = os.path.join(backup_root, "backup_log.txt")
with open(log_file, "a") as log:
    log.write(f"\nBackup started: {timestamp}\n")

    for name, source in folders_to_backup.items():
        backup_path = os.path.join(backup_root, f"{name}_Backup_{timestamp}")
        try:
            shutil.copytree(
                source,
                backup_path,
                ignore=shutil.ignore_patterns("~$*", "*.lock"),
                dirs_exist_ok=True,
                copy_function=shutil.copy2,
            )
            print(f"Backed up {name} successfully: {backup_path}")
            summary["success"] += 1
        except (PermissionError, FileNotFoundError, OSError) as e:
            print(f"Failed to back up {name}: {e}")
            summary["failed"] += 1
            # Log skipped files if possible
            if hasattr(e, "filename"):
                summary["skipped_files"].append(e.filename)
                log.write(f"Skipped: {e.filename} -> {e}\n")
            else:
                log.write(f"Failed folder {name} -> {e}\n")

    # Cleanup old backups (keep last 3 per folder)
    for folder_name in os.listdir(backup_root):
        folder_path = os.path.join(backup_root, folder_name)
        if os.path.isdir(folder_path):
            backups = sorted(
                [f for f in os.listdir(backup_root) if f.startswith(folder_name.split("_Backup")[0])],
                key=lambda x: os.path.getmtime(os.path.join(backup_root, x))
            )
            while len(backups) > 3:
                old = backups.pop(0)
                old_path = os.path.join(backup_root, old)
                try:
                    shutil.rmtree(old_path)
                    print(f"Deleted old backup: {old}")
                except (PermissionError, OSError) as e:
                    print(f"Could not delete {old}: {e}")
                    log.write(f"Could not delete {old} -> {e}\n")

    # Final summary
    print("\nSkipped locked/system files:")
    for f in summary["skipped_files"]:
        print(f"  - {f}")

    print(f"\nBackup finished: {summary['success']}/{len(folders_to_backup)} folders backed up successfully, {summary['failed']} failed. See backup_log.txt for details.")
