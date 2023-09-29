from config.db import app, db, ma

class Ciclovia_ruta(db.Model):
    __tablename__ = "tblciclovia_ruta"

    id = db.Column(db.Integer, primary_key = True)
    id_ciclovia = db.Column(db.Integer, db.ForeignKey('tblciclovia.id'))
    id_rutas = db.Column(db.Integer, db.ForeignKey('tblruta.id'))

    def __init__(self, id_ciclo, id_rut):
        self.id_ciclovia = id_ciclo
        self.id_rutas = id_rut
with app.app_context():
    db.create_all()

class Ciclovia_rutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_ciclovia','id_rutas')