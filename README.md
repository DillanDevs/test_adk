# 🌤️ Test Alphi - Agente Meteorólogo Especializado

Un proyecto basado en **Google ADK (Agent Development Kit)** que implementa un agente de IA especializado en meteorología. El agente proporciona información del clima actual, pronósticos meteorológicos y educación sobre fenómenos climáticos.

## 📋 Características

- **Agente de IA especializado** en meteorología usando Google Gemini
- **API REST** construida con FastAPI
- **Base de datos PostgreSQL** para manejo de sesiones
- **Herramientas personalizadas** para consultas meteorológicas
- **Interfaz web** incluida para interactuar con el agente
- **Contenedorización** con Docker y Docker Compose

## 🏗️ Arquitectura del Proyecto

```
Test_Alphi/
├── agents/
│   └── test_agent/
│       ├── __init__.py
│       └── agent.py          # Definición del agente meteorólogo
├── tools/
│   └── test_tool.py          # Herramientas para consultas de clima
├── docker-compose.yaml      # Configuración de servicios
├── Dockerfile               # Imagen del contenedor
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias de Python
└── README.md               # Este archivo
```

## ⚙️ Requisitos Previos

### Para ejecución local:
- **Python 3.11+** (recomendado 3.13)
- **PostgreSQL 15+** (opcional, solo para persistencia de sesiones)

### Para ejecución con Docker:
- **Docker** 20.10+
- **Docker Compose** 2.0+

## 🚀 Instalación y Ejecución

### Opción 1: Ejecución con Docker (Recomendado)

Esta es la forma más sencilla de ejecutar el proyecto, ya que Docker se encarga de todas las dependencias y configuraciones.

#### 2. Crear archivo de variables de entorno

Crear un archivo `.env` con el siguiente contenido:
```env
# Base de datos
SESSION_DB_URL=postgresql://adk_user:securepassword@db_test_aplhi:5432/adk_sessions

# Google API (si es necesario)
GOOGLE_API_KEY=tu_api_key_aqui
```

#### 3. Ejecutar con Docker Compose
```bash
# Construir y ejecutar todos los servicios
docker-compose up --build

# O ejecutar en segundo plano
docker-compose up -d --build
```

#### 4. Acceder a la aplicación
- **API**: http://localhost:8000
- **Documentación de la API**: http://localhost:8000/docs
- **Interfaz Web**: http://localhost:8000 (si está habilitada)
- **Base de datos PostgreSQL**: localhost:5432

#### 5. Detener los servicios
```bash
# Detener servicios
docker-compose down

# Detener y eliminar volúmenes (datos de la BD)
docker-compose down -v
```

### Opción 2: Ejecución Local con Python

#### 1. Crear entorno virtual

**En macOS/Linux:**
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
```

**En Windows:**
```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate
```

#### 2. Instalar dependencias
```bash
# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

#### 3. Configurar base de datos (Opcional)

**Opción A: Usar PostgreSQL local**
```bash
# Instalar PostgreSQL (macOS con Homebrew)
brew install postgresql
brew services start postgresql

# Crear base de datos
createdb adk_sessions
```

**Opción B: Usar PostgreSQL con Docker**
```bash
docker run -d \
  --name postgres-adk \
  -e POSTGRES_DB=adk_sessions \
  -e POSTGRES_USER=adk_user \
  -e POSTGRES_PASSWORD=securepassword \
  -p 5432:5432 \
  postgres:15-alpine
```

#### 4. Configurar variables de entorno
```bash
# Crear archivo .env
touch .env
```

Agregar el siguiente contenido al archivo `.env`:
```env
# Para base de datos local
SESSION_DB_URL=postgresql://adk_user:securepassword@localhost:5432/adk_sessions

GOOGLE_API_KEY=tu_api_key_aqui
```

#### 5. Ejecutar la aplicación
```bash
# Ejecutar con Python directamente
python main.py

# O con uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🛠️ Uso de la API

### Endpoints principales

- **GET** `/` - Página principal (interfaz web)
- **GET** `/docs` - Documentación de la API (Swagger)
- **POST** `/agents/{agent_name}/sessions` - Crear nueva sesión
- **POST** `/agents/{agent_name}/sessions/{session_id}/turn` - Enviar mensaje al agente

## 🔧 Desarrollo

### Agregar nuevas herramientas

1. Crear nueva función en `tools/` o agregar a `tools/test_tool.py`
2. Importar la función en `agents/test_agent/agent.py`
3. Agregar la herramienta al array `tools` del agente

### Modificar el agente

Editar el archivo `agents/test_agent/agent.py` para:
- Cambiar las instrucciones del agente
- Ajustar parámetros del modelo (temperatura, tokens, etc.)
- Agregar/quitar herramientas

### Variables de entorno disponibles

| Variable | Descripción | Requerido | Ejemplo |
|----------|-------------|-----------|---------|
| `SESSION_DB_URL` | URL de conexión a PostgreSQL | No | `postgresql://user:pass@host:5432/db` |
| `GOOGLE_API_KEY` | Clave API de Google | Depende | `AIza...` |

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'google.adk'"
```bash
# Verificar instalación de dependencias
pip install -r requirements.txt

# Si persiste el error, instalar específicamente:
pip install google-adk
```

### Error de conexión a base de datos
```bash
# Verificar que PostgreSQL esté ejecutándose
docker ps  # Para Docker
brew services list | grep postgresql  # Para macOS

# Verificar variables de entorno
echo $SESSION_DB_URL
```

### Puerto 8000 ya en uso
```bash
# Encontrar proceso usando el puerto
lsof -i :8000

# Cambiar puerto en .env
PORT=8001
```

### Problemas con Docker
```bash
# Limpiar contenedores y volúmenes
docker-compose down -v
docker system prune -f

# Reconstruir imágenes
docker-compose build --no-cache
```

## 📝 Logs y Debugging

### Ver logs en Docker
```bash
# Logs de todos los servicios
docker-compose logs

# Logs de un servicio específico
docker-compose logs api_test_aplhi
docker-compose logs db_test_aplhi

# Seguir logs en tiempo real
docker-compose logs -f
```

### Debugging local
```bash
# Ejecutar con logs detallados
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug

# O con Python
python -m uvicorn main:app --reload --log-level debug
```
