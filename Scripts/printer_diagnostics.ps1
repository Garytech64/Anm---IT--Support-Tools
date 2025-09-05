Write-Host "=== Printer Diagnostics Tool ===" -ForegroundColor Cyan

# List installed printers
$printers = Get-Printer
if ($printers) {
    Write-Host "`nInstalled Printers:" -ForegroundColor Green
    $printers | ForEach-Object { Write-Host " - $($_.Name)" }
} else {
    Write-Host "No printers found." -ForegroundColor Red
}

# Check spooler service
$spooler = Get-Service -Name Spooler -ErrorAction SilentlyContinue
if ($spooler.Status -eq "Running") {
    Write-Host "`nPrint Spooler service is running." -ForegroundColor Green
} else {
    Write-Host "`nPrint Spooler service is NOT running." -ForegroundColor Red
}
