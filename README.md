🌤️ Clima Ciudad
Aplicación en Python para consultar el clima de cualquier ciudad de forma sencilla y estructurada.
📋 Tabla de Contenidos
📖 Descripción
✨ Características
📁 Estructura del Proyecto
⚙️ Requisitos Previos
🚀 Instalación y Ejecución
🧪 Pruebas
📦 Dependencias
🔑 Variables de Entorno
👨‍💻 Uso
📄 Licencia
📖 Descripción
Clima Ciudad es una aplicación de línea de comandos que permite obtener información meteorológica actual de ciudades alrededor del mundo. Se conecta a una API de clima, procesa los datos y los muestra en un formato claro y legible. El proyecto está organizado siguiendo buenas prácticas de desarrollo, con separación de responsabilidades, configuración centralizada y pruebas automatizadas.
✨ Características
🔍 Consulta de clima por nombre de ciudad.
📊 Formateo de datos para una lectura amigable.
⚙️ Configuración centralizada y configurable mediante variables de entorno.
✅ Entrada de usuario validada y segura.
🧪 Pruebas unitarias implementadas con pytest.
🎨 Salida en consola con colores para mayor claridad.


📁 Estructura del Proyecto
plaintext
clima_ciudad/
├── 📂 .pytest_cache/          # Caché generada por pytest
├── 📂 config/                 # Configuración del proyecto
│   ├── __pycache__/
│   └── settings.py            # Ajustes generales y carga de variables
├── 📂 services/               # Lógica de negocio y conexión a API
│   ├── __pycache__/
│   ├── __init__.py
│   └── weather_service.py     # Llamadas a la API y procesamiento de datos
├── 📂 tests/                  # Pruebas unitarias
│   ├── __pycache__/
│   ├── __init__.py
│   └── test_weather_service.py
├── 📂 utils/                  # Funciones auxiliares
│   ├── __pycache__/
│   ├── formatter.py           # Formateo de datos para salida
│   └── user_input.py          # Manejo y validación de entrada del usuario
├── 📂 venv/                   # Entorno virtual de Python (no se sube a Git)
├── 📄 .env                    # Variables de entorno (claves API, etc.)
├── 📄 main.py                 # Punto de entrada de la aplicación
└── 📄 requirements.txt        # Lista de dependencias del proyecto



ℹ️ Nota: Las carpetas __pycache__/, .pytest_cache/ y venv/ 
son generadas automáticamente y no forman parte del código fuente que se edita.
⚙️ Requisitos Previos
Python 3.13 o superior 🐍
pip (gestor de paquetes de Python)
Acceso a internet (para consultar la API de clima)


🚀 Instalación y Ejecución
Clona o descarga este repositorio en tu equipo.
Crea y activa el entorno virtual:

# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Linux/macOS
source venv/bin/activate

Instala las dependencias:
bash
pip install -r requirements.txt
Configura tus variables de entorno:
Edita el archivo .env y agrega tu clave de API y otros ajustes necesarios.
Ejecuta la aplicación:
bash
python main.py
🧪 Pruebas
El proyecto usa pytest para las pruebas automatizadas. Para ejecutarlas:
bash
pytest tests/ -v

📦 Dependencias
Las librerías principales utilizadas son:
✅ requests: Para realizar peticiones HTTP a la API de clima.
✅ python-dotenv: Para cargar variables desde el archivo .env.
✅ colorama: Para dar color y formato a la salida en consola.
✅ pytest: Framework para escribir y ejecutar pruebas.
Todas están listadas en requirements.txt.


🔑 Variables de Entorno
El archivo .env debe contener al menos:
env
API_KEY=tu_clave_de_api_aqui
API_URL=https://api.ejemplo-clima.com/v1/weather
IDIOMA=es
UNIDADES=metric  # metric = °C, imperial = °F
🔒 Importante: Nunca compartas ni subas tu archivo .env al control de versiones.
👨‍💻 Uso
Al ejecutar main.py, la aplicación te pedirá ingresar el nombre de una ciudad. Escribe el nombre y presiona Enter. Verás algo como:
plaintext
🌍 Ingresa el nombre de la ciudad: Popayán

📍 Clima en Popayán, Colombia:
🌡️ Temperatura: 22°C
💧 Humedad: 78%
💨 Viento: 5 km/h
☁️ Estado: Cielo parcialmente nublado


📄 Licencia
Este proyecto es de uso libre para fines educativos y personales.
