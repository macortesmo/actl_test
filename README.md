# actl_test
Proyecto API rest en PY

<h2>Objetivo</h2>
API REST en Python bajo FastAPI que permite crear contactos en HubSport y suncronizar con ClickUp.

<h2>Instrucciones</h2>
1. Clonar repositorio.
2. Iniciar proyecto en terminal.
    El proyecto ya se encuentra inicializado y creada dependecias. En caso de no funcionar, correr lo siguiente:

    a. activiar el entrono virtual

      $ source env/bin/activate  # Para Linux/Mac
      $ env\Scripts\activate  # Para Windows

    b. Instalación de dependencias: Instala FastAPI, el cliente de HubSpot, el cliente de ClickUp y el conector de PostgreSQL ejecutando los siguientes comandos:
      $ pip install fastapi
      $ pip install httpx
      $ pip install pydantic
      $ pip install psycopg2
3. Detalle del proyecto: El proyecto contiene dos archivos, el primero config.py contiene las credenciales del proyecto y el segundo main.py contiene el codigo de la api
4. Inicializar API:
     Se procede a ejecutar el comando $ uvicorn main:app --reload en la terminal, de este modo se iniciará el servidor de desarrollo de FastAPI y podrás acceder a la API en http://localhost:8000.


