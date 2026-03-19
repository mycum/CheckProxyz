#!/bin/bash
echo "1. Загрузка баз прокси..."
curl -sL "https://github.com/igareck/vpn-configs-for-russia/raw/main/BLACK_SS+All_RUS.txt" > subs.txt
echo "" >> subs.txt

# БЕРЕМ ТОЛЬКО ТОП-200, а не всю сырую базу
curl -sL "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity.txt" >> subs.txt

echo "Скачано строк прокси:"
wc -l subs.txt

echo "2. Загрузка официального ядра LiteSpeedTest (v0.16.1)..."
wget -q -O lite.gz https://github.com/v2rayA/LiteSpeedTest/releases/download/v0.16.1/lite-linux-amd64-v0.16.1.gz
gunzip lite.gz
mv lite lite-linux-amd64
chmod +x ./lite-linux-amd64

echo "Проверка ядра:"
./lite-linux-amd64 --version

echo "3. Запуск глубокого тестирования..."
./lite-linux-amd64 --config lite_config.json --test subs.txt
