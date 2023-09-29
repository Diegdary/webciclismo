from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Usuario import Usuario , UsuarioSchema

ruta_usuario = Blueprint("ruta_usuario", __name__)

usuario_schema=UsuarioSchema()
usuarios_schema=UsuarioSchema(many=True)

@ruta_usuario.route("/usuarios", methods=["GET"])
def usuarios():
    resultall = Usuario.query.all() #select * from usuario
    result = usuarios_schema.dump(resultall)
    return jsonify(result)


@ruta_usuario.route("/saveusuario", methods=["POST"])
def saveusuarios():
    data= request.get_json()
    db.session.add(Usuario(**data))
    db.session.commit()
    return UsuarioSchema.jsonify(Usuario(**data))

@ruta_usuario.route("/updateusuario", methods=["PUT"])
def updateusuario():
    i = request.json["id"]
    nombre = request.json["nombre"]
    password = request.json["password"]
    genero = request.json["genero"]

    user = Usuario.query.get(i)
    user.nombre = nombre
    user.password = password
    user.genero = genero
    db.session.commit()
    return "guardado con exito!"

@ruta_usuario.route("/deleteusuario/<id>", methods=["GET"])
def deleteusuario(id):
    data = Usuario.query.get(i)
    db.session.delete(data)
    db.session.commit()
    return jsonify(UsuarioSchema.dump(data))




