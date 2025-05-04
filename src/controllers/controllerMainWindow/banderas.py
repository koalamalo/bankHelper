import os
import pycountry
from PySide6.QtGui import QPixmap, QIcon

FLAGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "media", "flags"))

flagsDown = [f for f in os.listdir(FLAGS_DIR) if f.endswith(".png")]
flagsDown.sort()

flags = []

for flag in flagsDown:
    code = flag.replace(".png", "").lower()

    if '-' in code:
        continue

    try:
        country = pycountry.countries.get(alpha_2=code.upper())
        flags.append({
            "filename": flag,
            "iso": country.alpha_3
        })
    except:
        print(f"⚠️  Código no reconocido: {code}")
        
flags= [{'filename': 'co.png', 'iso': 'COL'},
        {'filename': 'ar.png', 'iso': 'ARG'},
        {'filename': 'us.png', 'iso': 'USA'},
        {'filename': 'ca.png', 'iso': 'CAN'},]

def set_flag(flag_data, flagButton, iconsize):
        flag_filename = flag_data["filename"]
        flag_path = os.path.join(FLAGS_DIR, flag_filename)
        pixmap = QPixmap(flag_path)
        if pixmap.isNull():
            print(f"❌ Error: No se pudo cargar la imagen {flag_path}")
        else:
            flagButton.setIcon(QIcon(pixmap))
            flagButton.setIconSize(iconsize)
            flagButton.setFixedSize(iconsize.width()+20, iconsize.height()+20)
    
