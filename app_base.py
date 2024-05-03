from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#En este archivo seteamos la app de flask, inicalizamos el orm enganchado a la base de datos
#la razon por la que dejamos esto separado, es para poder primero importarlo en la carpeta de src/domain, en cada uno de los models.


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/code_first_db" # Aca podes apuntar a sqlite asi 'sqlite:///app.db'
db = SQLAlchemy(app)