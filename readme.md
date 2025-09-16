<!-- 
proyecto con Jinja2 para usar un template base, uso de bootstrap y separar el CSS en un archivo externo.
-->


# Instalaciones

# -- Entorno virtual
py -m venv .venv
# -- Acceso al entorno virtual
.venv\Scripts\Activate.ps1

pip install flask

# ejecución
python app.py

# ------------ clases de Bootstrap predefinidas
bg-primary → azul
bg-success → verde
bg-danger → rojo
bg-warning → amarillo
bg-info → celeste
bg-light → gris claro
bg-dark → gris oscuro

# Usar un color personalizado en style.css
le damos una clase personalizada a la navbar:
# en base.html:
<nav class="navbar navbar-expand-lg custom-navbar">

# en style.css
.custom-navbar {
    background-color: #0a2449;  /* Azul personalizado */
}
.custom-navbar .nav-link,
.custom-navbar .navbar-brand {
    color: #fff !important;  /* Texto blanco */
}

# Con gradiente
.custom-navbar {
    background: linear-gradient(90deg, #0a2449, #1e5f99);
}

## para salir del entorno virtual (.venv)
deactivate





# ------------------ PROJECT_04_DB: base de datos para almacenar la información de contacto ------------------

## Crear la base de datos en MySQL (XAMPP)
CREATE DATABASE contacto_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

## Instalar dependencias (en venv)
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv
pip install Flask-WTF  

# Nota: primero se deben realizar las instalaciones y crear el archivo .env y luego los demás archivos del proyecto

## estructura del proyecto
proyecto/
├─ app.py
├─ config.py
├─ models.py
├─ .env
├─ templates/
│  ├─ base.html
│  ├─ index.html
│  ├─ acerca.html
│  └─ contacto.html
└─ static/
   └─ style.css

# Índices para acelerar filtros por correo/fecha

--- agregar los índices en MySQL con:
CREATE INDEX ix_contact_messages_correo ON contact_messages (correo);
CREATE INDEX ix_contact_messages_created_at ON contact_messages (created_at);

ruta de registro de mensajes de contacto:
http://127.0.0.1:8080/admin/contactos




# ------ COMANDOS A TENER EN CUENTA

# para validar y mostrar información detallada del paquete python-dotenv
pip show python-dotenv

# listar las instalaciones
pip list
# Ver ruta de instalación
pip show flask | findstr Location
# para generar un archivo de dependencias
pip freeze > requirements.txt
# para instalar el archivo de dependencias generado
pip install -r requirements.txt
# Actualizar el archivo al agregar paquetes nuevos
pip freeze > requirements.txt

