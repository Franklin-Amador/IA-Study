import os
import json
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# TUS CREDENCIALES AQUÍ (las verás en Kaggle Account)
KAGGLE_NAME = os.getenv("KAGGLE_NAME")  # ← Cambia esto
KAGGLE_KEY = os.getenv("KAGGLE_KEY")           # ← Cambia esto

# Crear la carpeta .kaggle
kaggle_dir = os.path.expanduser('~/.kaggle')
os.makedirs(kaggle_dir, exist_ok=True)

# Crear el archivo kaggle.json
kaggle_json = {
    "username": KAGGLE_NAME,
    "key": KAGGLE_KEY
}

kaggle_path = os.path.join(kaggle_dir, 'kaggle.json')

with open(kaggle_path, 'w') as f:
    json.dump(kaggle_json, f, indent=2)

print(f"✓ kaggle.json creado en: {kaggle_path}")
print(json.dumps(kaggle_json, indent=2))