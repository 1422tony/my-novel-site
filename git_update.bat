@echo off
git add .
set /p msg="請輸入更新說明: "
git commit -m "%msg%"
git push
echo 更新完成！
pause