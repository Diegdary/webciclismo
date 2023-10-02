from flask import Blueprint, jsonify, request,json
from config.db import db, app, ma
from models.Ruta import Ruta , RutaSchema

ruta_ruta = Blueprint("ruta_ruta", __name__)

ruta_schema=RutaSchema()
rutas_schema=RutaSchema(many=True)

@ruta_ruta.route("/rutas", methods=["GET"])
def rutas():
    resultall = Ruta.query.all() #select * from ruta
    result = ruta_schema.dump(resultall)
    return jsonify(result)

@ruta_ruta.route("/saveruta", methods=["POST"])
def saveruta():
    data = request.get_json()
    db.session.add(Ruta(**data))
    db.session.commit()
    return jsonify(ruta_schema.dump(Ruta(**data)))

@ruta_ruta.route("/updateruta", methods=["PUT"])
def updateruta():
    i = request.json["id"]
    id_alerta = request.json["id_alerta"]
    id_usuario = request.json["id_usuario"]
    descripcion_ruta = request.json["descripcion_ruta"]
    nombre_ruta = request.json["nombre_ruta"]
    ciclovia_inicial = request.json["ciclovia_inicial"]
    ciclovia_final = request.json["ciclovia_final"]

    rutasx = Ruta.query.get(i)
    rutasx.id_alerta = id_alerta
    rutasx.id_usuario = id_usuario
    rutasx.descripcion_ruta = descripcion_ruta
    rutasx.nombre_ruta = nombre_ruta
    rutasx.ciclovia_inicial = ciclovia_inicial
    rutasx.ciclovia_final = ciclovia_final

    db.session.commit()
    return "guardado con exito!"
    
@ruta_ruta.route("/deleteruta/<id>", methods=["GET"])
def deleteruta(id):
    data = Ruta.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify(RutaSchema.dump(data))