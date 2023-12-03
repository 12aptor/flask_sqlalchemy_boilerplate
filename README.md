# Repaso Flask

## 1. Crear un entorno virtual

```bash
python -m venv "nombre del entorno"
```

## 2. Activar el entorno virtual

- Windows CMD
```bash
"nombre del entorno"\Scripts\activate
```
- Git bash
```bash
source "nombre del entorno"/Scripts/activate
```
- Linux/Mac
```bash
source "nombre del entorno"/bin/activate
```

## 3. Instalar Flask

```bash
pip install Flask
```

## 4. Crear el archivo requirements.txt

```bash
pip freeze > requirements.txt
```

## 5. Crear el archivo app.py

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo'

if __name__ == '__main__':
    app.run(debug=True)
```

## 6. Ejecutar el servidor

```bash
python app.py
```
ó
```bash
flask run
```

## 7. Crear el archivo .gitignore y agregar los archivos que no se subirán al repositorio

```bash
venv/
__pycache__
.env
...
```

## 8. Migramos a la base de datos

```bash
pip install Flask-Migrate
```

```python
from flask_migrate import Migrate
...
migrate = Migrate(app, db)
```

```bash
flask db init # Solo la primera vez (Crear la carpeta migrations)
flask db migrate -m "Initial migration." # Generar los documentos de migración
flask db upgrade # Ejecutar la migración
```