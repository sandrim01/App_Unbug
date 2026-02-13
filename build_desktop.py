import PyInstaller.__main__
import os
import shutil

# Remove previous build directories
if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("dist"):
    shutil.rmtree("dist")

PyInstaller.__main__.run([
    'desktop_app.py',
    '--name=UnbugERP',
    '--windowed', # Hide console
    '--onefile', # Single executable
    '--icon=app_icon.ico',
    '--add-data=templates;templates',
    '--add-data=static;static',
    '--add-data=blueprints;blueprints',
    '--add-data=generated-icon.png;.',
    '--hidden-import=engineio.async_drivers.threading',
    '--hidden-import=flask_sqlalchemy',
    '--hidden-import=flask_login',
    '--hidden-import=flask_wtf',
    '--hidden-import=email_validator',
    '--hidden-import=pystray',
    '--hidden-import=PIL',
    '--hidden-import=win10toast',
    '--hidden-import=flask_socketio',
    '--hidden-import=engineio',
    '--hidden-import=socketio',
    '--hidden-import=proxy_tools',
])

print("Build concluído com sucesso! O executável está na pasta 'dist'.")
