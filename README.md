##### Este microservicio permite crear, listar, enriquecer y buscar por similitud leads de restaurantes.

### Objetivo del proyecto:
    Crear leads de restaurantes
    Guardar leads en PostgreSQL usando SQLAlchemy
    Consumir API externa (API Ninjas) para obtener datos de ciudades
    Buscar leads similares usando una lógica de similitud básica
    Probado con Swagger y postman
    

### Tecnologias usadas
    Python 3.10+
    FastAPI
    SQLAlchemy
    PostgreSQL
    httpx
    python-dotenv
    Pydantic
    Uv
    Git + GitHub


### Crear y activar entorno virtual
    Windows PowerShell:
    pip install uv
### comprobar que esta instalado  
    uv --version  
### crea un entrono virtual
    uv venv
### activalo
    .\venv\Scripts\activate 
### pyproyect.toml
    uv sync
### instalar dependencias
    uv sync
    uv add fastapi[standard] sqlalchemy psycopg2 httpx python-dotenv

    
    
#### Instalar dependencias pip install -r requirements.txt uv pip freeze > requirements.txt #####

  
### Configurar la base de datos PostgreSQL
    Abrir PgAdmin o psql
    Crear base de datos:
    CREATE DATABASE leads_db; 
### Que la contraseña coincida


### Configuración de entorno
### Crea un archivo .env en la raíz del proyecto:
    DATABASE_URL=postgresql://postgres:contraseña@localhost:5432/nombredelatabla
    EXTERNAL_API_URL=https://api.api-ninjas.com/v1/geocoding
    EXTERNAL_API_KEY=TU_API_KEY_REAL


### Correr con uv
    uv run fastapi dev app/main.py


### Endpoints
### Health check
    GET /health

### Crear lead
    POST /api/leads
    {
  "name": "string",
  "city": "string",
  "phone": "string",
  "address": "string"
}

###### Ejemplo ####
    {
    "name": "crunchi",
    "city": "culiacan",
    "phone": "6674738591",
    "address": "valle alto",
  }


### Listar leads
  GET /api/leads

### Buscar leads similares
### ejemplo
name= crunchi  



### Pruebas en Postman

    http://localhost:8000/api/leads

    [
    {
        "name": "crunchi",
        "city": "culiacan",
        "phone": "6674738591",
        "address": "valle alto",
        "id": 1
    },
    {
        "name": "crunchi tec",
        "city": "culiacan",
        "phone": "6677905183",
        "address": "Guadalupe",
        "id": 2
    },
    {
        "name": "polaca",
        "city": "culiacan",
        "phone": "6688905533",
        "address": "conquista",
        "id": 3
    },
    {
        "name": "El Patio",
        "city": "Culiacán",
        "phone": "6670001122",
        "address": "barrancos",
        "id": 4
    },
    {
        "name": "El Patio",
        "city": "Culiacán",
        "phone": "6670001122",
        "address": "barrancos",
        "id": 5
    }
]




### Api externa utilizada
#### Este proyecto consume una API externa llamada API Ninjas, específicamente su endpoint de Geocoding, para obtener información geográfica de una ciudad ingresada por el usuario.

### La API recibe el nombre de la ciudad, la longitud, latitud, el pais y el estado.

    https://api.api-ninjas.com/v1/geocoding



















    
    