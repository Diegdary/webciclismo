from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Lugar_Estrategico import Lugar_EstrategicoSchema, Lugar_Estrategico

ruta_lugar_estrategico = Blueprint("ruta_lugar_estrategico", __name__)

lugarEstrategicoSchema = Lugar_EstrategicoSchema()
lugaresEstrategicoSchema = Lugar_EstrategicoSchema(many=True)

@ruta_lugar_estrategico.route("/lugares", methods=["GET"])
def lugares():
    resultall = Lugar_Estrategico.query.all()
    result = lugaresEstrategicoSchema.dump(resultall)
    return jsonify(result)

@ruta_lugar_estrategico.route("/savelugar", methods=["POST"])
def savelugar():
    data = request.get_json()
    db.session.add(Lugar_Estrategico(**data))
    db.session.commit()
    return jsonify(lugarEstrategicoSchema.dump(Lugar_Estrategico(**data)))

@ruta_lugar_estrategico.route("/updatelugar", methods=["PUT"])
def updatelugar():
    data = request.get_json()
    reg = Lugar_Estrategico.query.get(data["id"])
    reg.nombre = data["nombre"]
    reg.direccion = data["direccion"]

    db.session.commit()
    return jsonify(lugarEstrategicoSchema.dump(reg))


@ruta_lugar_estrategico.route("/deletelugar/<id>", methods=["GET"])
def deletelugar(id):
    data = Lugar_Estrategico.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(lugarEstrategicoSchema.dump(data))
