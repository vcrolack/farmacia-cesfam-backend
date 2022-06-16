# farmacia-cesfam-backend
Este es el repositorio contiene el backend del proyecto de [farmacia cesfam](https://github.com/vcrolack/farmacia-cesfam).

## Acerca del proyecto
Está escrito en Python utilizando el framework de FastAPI para realizar la interacción entre el front y la base de datos. Como ORM se usó SQLAlchemy.

## Pre requisitos
* Python 3.9.13
* FastAPI 0.78.0
* Entornos virtuales
* Revisar **requeriments.txt** para más información

## Correr el proyecto
1. clona el repositorio con `git clone https://github.com/vcrolack/farmacia-cesfam-backend.git`
2. Crea un entorno virtual de python con `python3 -m venv venv` (para windows `py -m venv venv` es válido también)
3. Ejecutar el archivo **requeriments.txt** con `pip install -r requeriments.txt` para instalar las dependencias del proyecto.
4. En el archivo **config/db.py** asegúrate de conectar el proyecto con una base de datos que hayas creado:
    1. en la línea 5, la variable engine, asegúrate de colocar la conexión con la siguiente sintaxis
    `engine = create_engine("mysql+pymysql://usuario_db:user_pass@host:port/nombre_db")`
5. Una vez configurado todo, arranca el proyecto con el siguiente comando `uvicorn main:app --reload` (puede ser sin el reload, solo es para recargar en caso de que haya cambios en el código).
6. Prueba los endpoints.

## Uso
Para utilizar el proyecto, FastAPI utiliza Swagger para crear una documentación automatizada e interactiva, solo ingresa a la url con la que se abre el proyecto y coloca /docs y podrás revisar y testear los endpoints. Ejemplo: `http://localhost:8000/docs`
