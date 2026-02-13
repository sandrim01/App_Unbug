from PIL import Image
import os

def convert_to_ico():
    if os.path.exists("generated-icon.png"):
        img = Image.open("generated-icon.png")
        # Resize to standard icon sizes if needed, but Pillow usually handles it
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save("app_icon.ico", sizes=icon_sizes)
        print("Icone convertido com sucesso para 'app_icon.ico'")
    else:
        print("Erro: 'generated-icon.png' não encontrado.")

if __name__ == "__main__":
    convert_to_ico()
