from flask import Flask, redirect, jsonify, render_template, request
from config.db import app

from api.Usuario import ruta_usuario

app.register_blueprint(ruta_usuario, url_prefix="/api")

@app.route("/")
def index():
    return "Hello!!"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')