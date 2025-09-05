@echo off
title ANM IT Support Tools
:MENU
cls
echo ================================
echo   ANM IT Support Tools Launcher
echo ================================
echo.
echo 1. Launch IT Monitoring Dashboard
echo 2. Run Printer Diagnostics (PowerShell)
echo 3. Run Backup Script (Python)
echo 4. Exit
echo.
set /p choice="Enter choice: "

if "%choice%"=="1" goto DASHBOARD
if "%choice%"=="2" goto PRINTER
if "%choice%"=="3" goto BACKUP
if "%choice%"=="4" exit
goto MENU

:DASHBOARD
cd /d %~dp0Dashboard
echo Starting ANM IT Monitoring Dashboard...
python app.py
pause
goto MENU

:PRINTER
cd /d %~dp0Scripts
powershell -ExecutionPolicy Bypass -File printer_diagnostics.ps1
pause
goto MENU

:BACKUP
cd /d %~dp0
python backup.py
pause
goto MENU
