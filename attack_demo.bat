@echo off
chcp 65001 >nul
echo --- ЗАПУСК ТЕСТА (WINDOWS) ---

:: Записываем первую ссылку
echo [CHAT] Scammer: Check this https://steeam-community.ru/trade >> dotaexp_logs.txt
echo [+] Ссылка 1 отправлена. Ждем 10 секунд...

timeout /t 10 >nul

:: Записываем вторую ссылку
echo [CHAT] Scammer: Free skins! https://steam-powered-security.com >> dotaexp_logs.txt
echo [+] Ссылка 2 отправлена.

echo --- ТЕСТ ЗАВЕРШЕН ---
pause