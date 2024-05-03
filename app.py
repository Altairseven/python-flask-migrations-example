from flask import Flask

from app_base import Migrate, app
#Importamos la db inicializada por SQL Alquemy, 
#luego de que paso por el archivo de context y importo los modelos que declaramos ahi.
from src.domain.context import db

migrate = Migrate(app, db)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"