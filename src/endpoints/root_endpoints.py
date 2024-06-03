from flask import Blueprint

root_endpoints = Blueprint("root", __name__)

@root_endpoints.get("/")
def index():
    return "<h1>Please use an /api route</h1>"

@root_endpoints.get("/api")
def api_index():
    return "<h1>Ok</h1>"