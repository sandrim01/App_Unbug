import webview
import multiprocessing
import uvicorn
import sys
import os
import time
import socket
from api.main import app

def run_backend():
    uvicorn.run(app, host="127.0.0.1", port=8000)

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

if __name__ == '__main__':
    # No Windows, multiprocessing precisa disso
    multiprocessing.freeze_support()
    
    # Inicia o backend em um processo separado
    backend_process = multiprocessing.Process(target=run_backend, daemon=True)
    backend_process.start()
    
    # Aguarda o backend subir
    print("Iniciando Unbug ERP...")
    for _ in range(10):
        if is_port_open(8000):
            break
        time.sleep(1)

    # URL do frontend (em dev usamos o localhost do next, em prod usaremos o backend servindo os estáticos)
    # Por enquanto, como estamos desenvolvendo, vamos assumir que o usuário rodará o next dev.
    # Mas para o "WOW" moment, vamos tentar abrir a API primeiro.
    url = "http://localhost:3000" 
    
    # Se o Next não estiver rodando, abre a documentação da API como fallback
    if not is_port_open(3000):
        print("Frontend Next.js não detectado na porta 3000. Abrindo API Docs...")
        url = "http://127.0.0.1:8000/docs"

    window = webview.create_window(
        'Unbug ERP 2.0', 
        url,
        width=1280,
        height=800,
        min_size=(1000, 700),
        background_color='#020617'
    )
    
    webview.start()
    
    # Cleanup ao fechar
    backend_process.terminate()
