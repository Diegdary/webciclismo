from flask import Flask, redirect, jsonify, render_template, request, session
from config.db import app, db
from models.Usuario import Usuario, UsuarioSchema

from api.Usuario import ruta_usuario
from api.comunidad import ruta_comunidad
from api.Alerta import ruta_alerta
from api.Ruta import ruta_ruta


app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_comunidad, url_prefix="/api")
app.register_blueprint(ruta_alerta, url_prefix="/api")
app.register_blueprint(ruta_ruta, url_prefix="/api")


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/ingresar", methods=["POST"])
def ingresar():
    usuario= request.form["username"]
    password= request.form["password"]
    userr = db.session.query(Usuario.id).filter(Usuario.nombre == usuario, Usuario.password == password).all()
    resultado = UsuarioSchema(many=True).dump(userr)
    
    if len(resultado) > 0:
        session["usuario"]=usuario
        return redirect("/home")
    else:
        return redirect("/")
    

@app.route("/comunidad", methods=["GET"])
def comunidad():
    if "usuario" in session:
        return render_template("comunidad.html", usuario= session["usuario"])
    else:
        return redirect("/")
    
@app.route("/alertas", methods=["GET"])
def alertas():
    if "usuario" in session:
        return render_template("alertas.html", usuario= session["usuario"])
    else:
        return redirect("/")
    
@app.route("/home", methods=["GET"])
def home():
    if "usuario" in session:
        return render_template("home.html", usuario= session["usuario"])
    else:
        return redirect("/")
    

@app.route("/rutas", methods=["GET"])
def rutas():
    if "usuario" in session:
        return render_template("rutas.html", usuario= session["usuario"])
    else:
        return redirect("/")



@app.route("/salir")
def salir():
    session.pop("usuario",None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')