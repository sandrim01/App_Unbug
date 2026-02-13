import os
import sys
import threading
import time
import webview
from app import app, socketio
import pystray
from PIL import Image
from win10toast import ToastNotifier
import ctypes

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

toaster = ToastNotifier()

def show_notification(title, message):
    try:
        toaster.show_toast(
            title,
            message,
            icon_path=resource_path("generated-icon.png"),
            duration=5,
            threaded=True
        )
    except:
        pass

def run_flask():
    socketio.run(app, host="127.0.0.1", port=5000, debug=False, use_reloader=False)

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def show_window(icon, item):
    window.show()

def setup_tray():
    image = Image.open(resource_path("generated-icon.png"))
    menu = pystray.Menu(
        pystray.MenuItem("Abrir Unbug ERP", show_window),
        pystray.MenuItem("Sair", on_quit)
    )
    icon = pystray.Icon("UnbugERP", image, "Unbug Solutions TI", menu)
    icon.run()

if __name__ == "__main__":
    # Ensure High DPI support on Windows
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Wait a bit for Flask to start
    time.sleep(2)

    # Create the webview window
    window = webview.create_window(
        'Unbug Solutions TI - ERP',
        'http://127.0.0.1:5000',
        width=1280,
        height=720,
        min_size=(1024, 768),
        confirm_close=True,
        background_color='#121212'
    )

    # Start System Tray in a separate thread
    tray_thread = threading.Thread(target=setup_tray)
    tray_thread.daemon = True
    tray_thread.start()

    # Start the webview GUI
    webview.start()
