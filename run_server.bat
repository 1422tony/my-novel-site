@echo off
:: 強制切換到 .bat 檔案所在的資料夾
cd /d %~dp0

echo 伺服器啟動中...
echo 請確認手機已連上 Tailscale
echo 你的 Tailscale IP 可以在系統右下角圖示查看
echo.

:: 啟動伺服器
python -m http.server 8000

pause