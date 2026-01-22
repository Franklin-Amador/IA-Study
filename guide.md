# Guía de Configuración Inicial

## Paso 1: Crear el Entorno Virtual

Ejecuta el siguiente comando para crear un entorno virtual:

```bash
python -m venv venv
```

Activa el entorno virtual:

- **Windows:**

    ```bash
    venv\Scripts\activate
    ```

- **Linux/Mac:**

    ```bash
    source venv/bin/activate
    ```

## Paso 2: Instalar Dependencias

Ejecuta el `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Paso 3: Obtener Datos del Capítulo 2

Ejecuta el script `data.py` para descargar y procesar los datos, en el se genera la estructura de la carpeta datasets:

```bash
python data.py
```

Una vez completados estos pasos, tendrás todo configurado para comenzar.

## Paso 4: Configurar el kaggle downloader

Para ello ocuparemos una variable de entorno con la key `KAGGLE_KEY` y `KAGGLE_NAME` con ello nos iremos a my_kaggle.py y lo ejecutaremos,
posteriormente podremos descargar cualquier csv solo cambiando la url de kaggle. Por defecto estará el csv de steam, puedes descargar
cualquiera que gustes y crear tus propios proyectos.
