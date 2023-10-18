from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Alerta import Alerta , AlertaSchema

ruta_alerta = Blueprint("ruta_alerta", __name__)

alerta_schema=AlertaSchema()
alertas_schema=AlertaSchema(many=True)

@ruta_alerta.route("/alertas", methods=["GET"])
def alertas():
    resultall = Alerta.query.all() #select * from alerta
    print(resultall)
    result = alertas_schema.dump(resultall)
    print(result)
    return jsonify(result)


@ruta_alerta.route("/savealerta", methods=["POST"])
def savealerta():
    data = request.get_json()
    db.session.add(Alerta(**data))
    db.session.commit()
    return jsonify(alerta_schema.dump(Alerta(**data)))


@ruta_alerta.route("/updatealerta", methods=["PUT"])
def updatealerta():
    i = request.json["id"]
    zonas_peligrosas = request.json["zonas_peligrosas"]
    intersecciones = request.json["intersecciones"]
    cambio_clima = request.json["cambio_clima"]
    fecha_alerta = request.json["fecha_alerta"]

    alert = Alerta.query.get(i)
    alert.zonas_peligrosas = zonas_peligrosas
    alert.intersecciones = intersecciones
    alert.cambio_clima = cambio_clima
    alert.fecha_alerta = fecha_alerta

    db.session.commit()
    return "guardado con exito!"


@ruta_alerta.route("/deletealerta/<id>", methods=["GET"])
def deletealerta(id):
    data = Alerta.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(alerta_schema.dump(data))
