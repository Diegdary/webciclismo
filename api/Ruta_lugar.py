from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Ruta_lugar import Ruta_lugar , Ruta_lugarSchema

ruta_ruta_lugar = Blueprint("ruta_ruta_lugar", __name__)

ruta_lugarschema=Ruta_lugarSchema()
rutas_lugarschema=Ruta_lugarSchema(many=True)

@ruta_ruta_lugar.route("/rutaslugar", methods=["GET"])
def rutaslugar():
    resultall = Ruta_lugar.query.all() #select * from ruta
    result = rutas_lugarschema.dump(resultall)
    return jsonify(result)

@ruta_ruta_lugar.route("/saverutalugar", methods=["POST"])
def saverutalugar():
    data = request.get_json()
    db.session.add(Ruta_lugar(**data))
    db.session.commit()
    return jsonify(ruta_lugarschema.dump(Ruta_lugar(**data)))

@ruta_ruta_lugar.route("/updaterutalugar", methods=["PUT"])
def updaterutalugar():
    i = request.json["id"]
    id_ruta = request.json["id_ruta"]
    id_lugar = request.json["id_lugar"]

    rutalugar = Ruta_lugar.query.get(i)
    rutalugar.id_ruta = id_ruta
    rutalugar.id_lugar = id_lugar
    
    db.session.commit()
    return "guardado con exito!"

@ruta_ruta_lugar.route("/deleterutalugar/<id>", methods=["GET"])
def deleterutalugar(id):
    data = Ruta_lugar.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(ruta_lugarschema.dump(data))

