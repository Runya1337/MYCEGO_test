@echo off
echo Checking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed.
    echo Please install Python from the official website: https://www.python.org/
    pause
    exit
)

echo Installing required libraries...
python -m pip install -r requirements.txt
pip3 install tkinter
echo Running the script...
python main.py

echo Script executed successfully.
pause
