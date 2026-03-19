#!/bin/bash
# Загрузка LiteSpeedTest
wget -O lite-linux-amd64 https://github.com/FacePork/LiteSpeedTest/releases/download/v0.15.0/lite-linux-amd64
chmod +x ./lite-linux-amd64

# Запуск теста. Результат будет в out.json
./lite-linux-amd64 --config lite_config.json --test subs
