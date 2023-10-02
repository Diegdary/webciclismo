from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Ciclovia_ruta import Ciclovia_ruta , Ciclovia_rutaSchema

ruta_ciclovia_ruta = Blueprint("ruta_ciclovia_ruta", __name__)

ciclovia_ruta_schema=Ciclovia_rutaSchema()
ciclovias_ruta_schema=Ciclovia_rutaSchema(many=True)

@ruta_ciclovia_ruta.route("/cicloviasruta", methods=["GET"])
def cicloviasruta():
    resultall = Ciclovia_ruta.query.all() #select * from ruta
    result = ciclovia_ruta_schema.dump(resultall)
    return jsonify(result)

@ruta_ciclovia_ruta.route("/savecicloviaruta", methods=["POST"])
def savecicloviaruta():
    data = request.get_json()
    db.session.add(Ciclovia_ruta(**data))
    db.session.commit()
    return jsonify(ciclovia_ruta_schema.dump(Ciclovia_ruta(**data)))

@ruta_ciclovia_ruta.route("/updatecicloviaruta", methods=["PUT"])
def updatecicloviaruta():
    i = request.json["id"]
    id_ciclovia = request.json["id_ciclovia"]
    id_rutas = request.json["id_rutas"]
    

    cicloviasruta = Ciclovia_ruta.query.get(i)
    cicloviasruta.id_ciclovia = id_ciclovia
    cicloviasruta.id_rutas = id_rutas

    db.session.commit()
    return "guardado con exito!"

@ruta_ciclovia_ruta.route("/deletecicloviaruta/<id>", methods=["GET"])
def deletecicloviaruta(id):
    data = Ciclovia_ruta.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(Ciclovia_rutaSchema.dump(data))