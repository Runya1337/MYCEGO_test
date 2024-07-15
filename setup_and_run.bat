@echo off
echo Проверка наличия Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не установлен.
    echo Пожалуйста, установите Python с официального сайта: https://www.python.org/
    pause
    exit
)

echo Установка необходимых библиотек...
python -m pip install -r requirements.txt
pip3 install tkinter
echo Запуск скрипта...
python main.py

echo Скрипт выполнен успешно.
pause
