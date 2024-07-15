#!/bin/bash

# Проверка наличия Python и его установка, если он отсутствует
if ! command -v python3 &> /dev/null; then
    echo "Python3 не установлен. Установка Python..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
    echo "Python установлен."
else
    echo "Python уже установлен."
fi

# Создание виртуального окружения, если оно не создано
if [ ! -d "venv" ]; then
    echo "Создание виртуального окружения..."
    python3 -m venv venv
    if [ $? -eq 0 ]; then
        echo "Виртуальное окружение создано."
    else
        echo "Не удалось создать виртуальное окружение."
        exit 1
    fi
fi

# Активация виртуального окружения
echo "Активация виртуального окружения..."
source venv/bin/activate
if [ $? -eq 0 ]; then
    echo "Виртуальное окружение активировано."
else
    echo "Не удалось активировать виртуальное окружение."
    exit 1
fi

# Обновление pip и установка зависимостей из файла requirements.txt
echo "Установка и обновление необходимых библиотек..."
pip install --upgrade pip
brew install python-tk
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "Зависимости установлены."
else
    echo "Ошибка при установке зависимостей."
    deactivate
    exit 1
fi

# Запуск скрипта Python
echo "Запуск скрипта..."
python3 main.py
if [ $? -eq 0 ]; then
    echo "Скрипт выполнен успешно."
else
    echo "Ошибка выполнения скрипта."
fi

# Деактивация виртуального окружения
deactivate
echo "Виртуальное окружение деактивировано."
