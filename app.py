from flask import Flask, redirect, jsonify, render_template, request
from config.db import app

from api.Usuario import ruta_usuario
from api.Ciclovia import ruta_ciclovia
from api.Lugar_estrategico import ruta_lugar_estrategico
from api.comunidad import ruta_comunidad
from api.Alerta import ruta_alerta

app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_ciclovia, url_prefix="/api")
app.register_blueprint(ruta_lugar_estrategico, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_alerta, url_prefix="/api")

@app.route("/")
def index():
    return "Hello!!"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')