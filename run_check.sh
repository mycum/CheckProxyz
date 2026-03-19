#!/bin/bash
echo "Загрузка баз прокси..."
curl -sL "https://github.com/igareck/vpn-configs-for-russia/raw/main/BLACK_SS+All_RUS.txt" > subs.txt
echo "" >> subs.txt
# Используем txt-версию базы mahdibland, она идеально подходит для тестера
curl -sL "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt" >> subs.txt

echo "Установка тестера..."
wget -q -O lite-linux-amd64 https://github.com/FacePork/LiteSpeedTest/releases/download/v0.15.0/lite-linux-amd64
chmod +x ./lite-linux-amd64

echo "Старт проверки..."
./lite-linux-amd64 --config lite_config.json --test subs.txt
