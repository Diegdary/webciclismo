from config.db import app, db, ma

class Ruta(db.Model):
    __tablename__ = "tblruta"

    id = db.Column(db.Integer, primary_key = True)
    id_alerta = db.Column(db.Integer, db.ForeignKey('tblalerta.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    descripcion_ruta = db.Column(db.String(50))
    nombre_ruta = db.Column(db.String(50))
    ciclovia_inicial = db.Column(db.String(50))
    ciclovia_final = db.Column(db.String(50))

    def __init__(self,id_alerta,id_usuario,descripcion_ruta,nombre_ruta,ciclovia_inicial,ciclovia_final):
        self.id_alerta = id_alerta
        self.id_usuario = id_usuario
        self.descripcion_ruta = descripcion_ruta
        self.nombre_ruta = nombre_ruta
        self.ciclovia_inicial = ciclovia_inicial
        self.ciclovia_final = ciclovia_final

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_alerta','id_usuario','descripcion_ruta', 'nombre_ruta', 'ciclovia_inicial', 'ciclovia_final')