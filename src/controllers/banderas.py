import os
import pycountry

FLAGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "media", "flags"))

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

def flagButtonInit(nextFlagButton):
    nextFlagButton.setVisible(False)
    nextFlagButton.setFlat(True)
    nextFlagButton.setStyleSheet("background: transparent; border: none;")
    
    