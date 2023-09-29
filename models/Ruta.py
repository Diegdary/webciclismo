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

    def __init__(self,a,b,c,d,f,g):
        self.id_alerta = a
        self.id_usuario = b
        self.descripcion_ruta = c
        self.nombre_ruta = d
        self.ciclovia_inicial = f
        self.ciclovia_final = g

with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_alerta','id_usuario','descripcion_ruta', 'nombre_ruta', 'ciclovia_inicial', 'ciclovia_final')