
from flask import Blueprint

student_endpoints = Blueprint("students", __name__)

@student_endpoints.get("/")
def index():
    return "<h1>Hello, World student!</h1>"





