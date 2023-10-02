from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Ciclovia import Ciclovia , CicloviaSchema

ruta_ciclovia = Blueprint("ruta_ciclovia", __name__)

ciclovia_schema = CicloviaSchema()
ciclovias_schema = CicloviaSchema(many=True)

@ruta_ciclovia.route("/ciclovias", methods=["GET"])
def ciclovias():
    resultall = Ciclovia.query.all() #select * from ciclovias
    result = ciclovias_schema.dump(resultall)
    return jsonify(result)

@ruta_ciclovia.route("/saveciclovia", methods=["POST"])
def saveciclovia():
    data = request.get_json()
    db.session.add(Ciclovia(**data))
    db.session.commit()
    return jsonify(ciclovia_schema.dump(Ciclovia(**data)))


@ruta_ciclovia.route("/updateciclovia", methods=["PUT"])
def updateciclovia():
    data = request.get_json()
    reg = Ciclovia.query.get(data["id"])
    reg.punto_inicial= data["punto_inicial"]
    reg.punto_final= data["punto_final"]
    reg.descripcion= data["descripcion"]
    reg.nombre_ciclovia= data["nombre_ciclovia"]

    db.session.commit()
    return jsonify(ciclovia_schema.dump(reg))


@ruta_ciclovia.route("/deleteciclovia/<id>", methods=["GET"])
def deleteciclovia(id):
    data = Ciclovia.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(ciclovia_schema.dump(data))

