import csv
from datetime import datetime

# Sample mailbox data
mailboxes = [
    {"Name": "John Doe", "Email": "j.doe@example.com", "MailboxSize": "2GB"},
    {"Name": "Jane Smith", "Email": "j.smith@example.com", "MailboxSize": "1.5GB"},
]

# Export to CSV
filename = f"MailboxReport_{datetime.now().strftime('%Y%m%d')}.csv"
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ["Name", "Email", "MailboxSize"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for mailbox in mailboxes:
        writer.writerow(mailbox)

print(f"Mailbox report generated: {filename}")
