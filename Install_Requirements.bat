@echo off
title LumiaSend Setup
echo ========================================================
echo   LUMIASEND: ONE-CLICK ENVIRONMENT SETUP
echo ========================================================
echo.

:: 1. CHECK FOR PYTHON
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is NOT installed.
    echo [!] Opening the download page... 
    echo.
    echo IMPORTANT: Check the "Add Python to PATH" box in the installer!
    timeout /t 5
    start https://www.python.org/downloads/windows/
    pause
    exit
)

echo [OK] Python detected.

:: 2. ENSURE PIP IS INSTALLED & UPDATED
echo [1/2] Preparing package manager (pip)...
python -m ensurepip --default-pip >nul 2>&1
python -m pip install --upgrade pip --quiet

:: 3. INSTALL LUMIASEND LIBRARIES
echo [2/2] Installing LumiaSend dependencies...
python -m pip install flask flask-cors

echo.
echo ========================================================
echo   SUCCESS: Your PC is ready for LumiaSend!
echo ========================================================
echo.
echo You can now run your LumiaSend server script.
echo.
pause