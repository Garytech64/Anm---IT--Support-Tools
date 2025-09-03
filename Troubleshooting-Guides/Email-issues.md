
---

## **Email-Issues.md**

```markdown
# Email Troubleshooting Guide

## Common Issues
- Cannot send or receive emails
- Outlook not connecting to Exchange/Office 365
- Emails stuck in Outbox
- Login or authentication errors

## Step-by-Step Troubleshooting

### 1. Check Connectivity
- Verify internet connection.
- Check Office 365 service status: [https://status.office.com](https://status.office.com)

### 2. Verify Credentials
- Ensure username and password are correct.
- If MFA is enabled, verify authentication.

### 3. Restart and Reconfigure
- Close and reopen Outlook.
- Remove and re-add the email account if necessary.

### 4. Check Mailbox
- Verify mailbox isn’t full.
- Check for any email forwarding or rules that may block delivery.

### 5. Clear Cache
- Clear Outlook cache and temporary files.
```powershell
del %localappdata%\Microsoft\Outlook\*.ost
