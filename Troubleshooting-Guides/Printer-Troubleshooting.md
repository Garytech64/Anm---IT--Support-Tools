# Printer Troubleshooting Guide

## Common Issues
- Printer not responding / offline
- Print jobs stuck in queue
- Users cannot connect to network printer
- Poor print quality (lines, streaks, faded text)

## Step-by-Step Troubleshooting

### 1. Check Hardware
- Verify printer is powered on and connected to the network (Ethernet/Wi-Fi).
- Check for paper jams or low toner/ink.

### 2. Check Printer Status
- On Windows: Go to **Control Panel > Devices and Printers**.
- Ensure the printer is set as **default** and **Online**.
- Clear any stuck print jobs.

### 3. Restart Services
- Restart the **Print Spooler Service**:
```powershell
Stop-Service spooler
Start-Service spooler
