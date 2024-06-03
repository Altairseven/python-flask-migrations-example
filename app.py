from flask import Flask

from src.endpoints.root_endpoints import root_endpoints
from src.endpoints.students_endpoints import student_endpoints

from app_base import Migrate, app
#Importamos la db inicializada por SQL Alquemy, 
#luego de que paso por el archivo de context y importo los modelos que declaramos ahi.
from src.domain.context import db

migrate = Migrate(app, db)

app.register_blueprint(root_endpoints, url_prefix="/")
app.register_blueprint(student_endpoints, url_prefix="/api/students")