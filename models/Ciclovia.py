from config.db import app, db, ma

class Ciclovia(db.Model):
    __tablename__ = "ciclovia"

    id = db.Column(db.Integer, primary_key = True)
    punto_inicial = db.Column(db.String(50))
    punto_final = db.Column(db.String(50))
    descripcion = db.Column(db.String(50))
    nombre_ciclovia = db.Column(db.String(50))

    def __init__(self, pinicial, pfinal, desc, nciclo):
        self.punto_inicial = pinicial
        self.punto_final = pfinal
        self.descripcion = desc
        self.nombre_ciclovia = nciclo
with app.app_context():
    db.create_all()

class CicloviaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'punto_inicial','punto_final','descripcion','nombre_ciclovia')  