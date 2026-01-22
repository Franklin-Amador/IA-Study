# download_kaggle_dataset.py
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_kaggle_dataset(dataset_name, output_base='./datasets', only_csv=True):
    """
    Descarga un dataset de Kaggle de forma organizada
    
    Args:
        dataset_name: nombre del dataset en formato 'owner/dataset-name'
        output_base: carpeta base para datasets (default: './datasets')
        only_csv: si True, solo guarda archivos CSV (default: True)
    
    Example:
        download_kaggle_dataset('fronkongames/steam-games-dataset')
    """
    try:
        # Verificar que kaggle.json existe
        kaggle_json_path = os.path.expanduser('~/.kaggle/kaggle.json')
        if not os.path.exists(kaggle_json_path):
            raise FileNotFoundError(
                f"❌ No se encontró kaggle.json en {kaggle_json_path}\n"
                f"Por favor:\n"
                f"1. Descárgalo desde https://www.kaggle.com/account\n"
                f"2. Muévelo a {kaggle_json_path}"
            )
        
        # Extraer nombre limpio del dataset
        dataset_folder_name = dataset_name.split('/')[-1]
        output_path = os.path.join(output_base, dataset_folder_name)
        
        print(f"📥 Descargando dataset: {dataset_name}")
        print(f"📁 Carpeta destino: {output_path}")
        
        # Autenticar
        api = KaggleApi()
        api.authenticate()
        print("✓ Autenticación exitosa")
        
        # Crear carpetas necesarias
        os.makedirs(output_path, exist_ok=True)
        temp_path = os.path.join(output_path, 'temp')
        os.makedirs(temp_path, exist_ok=True)
        
        # Descargar dataset (comprimido)
        print("⏳ Descargando archivos...")
        api.dataset_download_files(
            dataset_name,
            path=temp_path,
            unzip=False  # No descomprimir automáticamente
        )
        
        # Buscar el archivo ZIP descargado
        zip_files = [f for f in os.listdir(temp_path) if f.endswith('.zip')]
        
        if not zip_files:
            print("❌ No se encontró archivo ZIP descargado")
            return False
        
        zip_path = os.path.join(temp_path, zip_files[0])
        print(f"✓ Archivo descargado: {zip_files[0]}")
        
        # Extraer solo archivos CSV (o todos si only_csv=False)
        print("📦 Extrayendo archivos...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            all_files = zip_ref.namelist()
            
            if only_csv:
                # Filtrar solo CSV
                files_to_extract = [f for f in all_files if f.endswith('.csv')]
            else:
                # Extraer todos menos JSON
                files_to_extract = [f for f in all_files if not f.endswith('.json')]
            
            # Extraer archivos filtrados
            for file in files_to_extract:
                zip_ref.extract(file, output_path)
                print(f"  ✓ Extraído: {file}")
        
        # Limpiar archivos temporales
        import shutil
        shutil.rmtree(temp_path)
        print("🧹 Archivos temporales eliminados")
        
        # Listar archivos finales
        csv_files = [f for f in os.listdir(output_path) if f.endswith('.csv')]
        
        print(f"\n✅ Descarga completa en: {os.path.abspath(output_path)}")
        print(f"📊 Archivos CSV descargados ({len(csv_files)}):")
        
        for file in csv_files:
            file_path = os.path.join(output_path, file)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f"  - {file} ({size_mb:.2f} MB)")
        
        return True
        
    except FileNotFoundError as e:
        print(e)
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Ejemplos de uso:
    
    # Dataset de Steam
    download_kaggle_dataset('fronkongames/steam-games-dataset')
    
    # Otros datasets (descomenta para usar)
    # download_kaggle_dataset('camnugent/california-housing-prices')
    # download_kaggle_dataset('kemical/kickstarter-projects')