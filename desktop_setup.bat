@echo off
echo ===================================================
echo   Unbug ERP - Gerador de Executavel Windows
echo ===================================================
echo.
echo Verificando dependencias...
pip install pyinstaller pywebview pystray Pillow win10toast flask-socketio

echo.
echo Iniciando o build com PyInstaller...
python build_desktop.py

echo.
if exist "dist\UnbugERP.exe" (
    echo [SUCESSO] O executavel foi gerado em: dist\UnbugERP.exe
) else (
    echo [ERRO] Falha ao gerar o executavel. Verifique os logs acima.
)
pause
