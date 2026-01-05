#!/bin/bash

LOG_FILE="dotaexp_logs.txt"

echo "--- ЗАПУСК ТЕСТА С ПАУЗАМИ ---"

# Первая ссылка
echo "[CHAT] Scammer: Check this https://steeam-community.ru/trade" >> "$LOG_FILE"
sync # Сбрасывает буфер на диск
echo "[+] Ссылка 1 отправлена. Ждем 30 секунд..."

sleep 30

# Вторая ссылка
echo "[CHAT] Scammer: Win skins here https://steam-powered-security.com" >> "$LOG_FILE"
sync
echo "[+] Ссылка 2 отправлена."
