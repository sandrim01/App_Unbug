@echo off
echo ==========================================
echo    INICIANDO UNBUG ERP 2.0 (MODERNO)
echo ==========================================

start cmd /k "cd web && npm run dev"
echo Aguardando Next.js iniciar...
timeout /t 5

echo Iniciando Backend e App Desktop...
python desktop_app.py

pause
