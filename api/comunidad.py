from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.comunidad import Comunidad, ComunidadSchema

ruta_comunidad = Blueprint("ruta_comunidad", __name__)

comunidad_schema = ComunidadSchema()
comunidades_schema = ComunidadSchema(many=True)

@ruta_comunidad.route("/comunidades", methods=["GET"])
def comunidades():
    data = Comunidad.query.all()
    result= comunidades_schema.dump(data)
    return jsonify(result) 

@ruta_comunidad.route("/savecomunidad", methods=["POST"])
def savecomunidad():
    data = request.get_json()
    result = Comunidad(**data)
    db.session.add(result)
    db.session.commit()
    return jsonify(comunidad_schema.dump(result))

@ruta_comunidad.route("/updatecomunidad", methods=["PUT"])
def updatecomunidad():
    data = request.get_json()
    result = Comunidad.query.get(data["id"])
    result.id_usuario= data["id_usuario"]
    result.mensaje = data["mensaje"]

    db.session.commit()
    return jsonify(comunidad_schema.dump(result))


@ruta_comunidad.route("/deletecomunidad/<id>", methods=["GET"])
def deletecomunidad(id):
    data = Comunidad.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return jsonify(comunidad_schema.dump(data))
