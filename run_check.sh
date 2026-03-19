#!/bin/bash
echo "1. Загрузка баз прокси..."
curl -sL "https://github.com/igareck/vpn-configs-for-russia/raw/main/BLACK_SS+All_RUS.txt" > subs.txt
echo "" >> subs.txt
curl -sL "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/Eternity.txt" >> subs.txt

echo "Скачано строк прокси:"
wc -l subs.txt

echo "2. Загрузка стабильного ядра LiteSpeedTest (v1.0.0)..."
wget -q -O lite-linux-amd64 https://github.com/mahdibland/SSAggregator/releases/download/1.0.0/lite-linux-amd64
chmod +x ./lite-linux-amd64

echo "3. Запуск глубокого тестирования..."
./lite-linux-amd64 --config lite_config.json --test subs.txt
