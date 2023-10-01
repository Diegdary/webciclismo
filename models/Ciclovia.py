from config.db import app, db, ma

class Ciclovia(db.Model):
    __tablename__ = "tblciclovia"

    id = db.Column(db.Integer, primary_key = True)
    punto_inicial = db.Column(db.String(50))
    punto_final = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    nombre_ciclovia = db.Column(db.String(50))

    def __init__(self, punto_inicial, punto_final, descripcion, nombre_ciclovia):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
        self.descripcion = descripcion
        self.nombre_ciclovia = nombre_ciclovia
with app.app_context():
    db.create_all()

class CicloviaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'punto_inicial','punto_final','descripcion','nombre_ciclovia')  