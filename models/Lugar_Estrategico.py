from config.db import app, db, ma

class Lugar_Estrategico(db.Model):
    __tablename__ = "tbllugar_estrategico"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))

    def __init__(self, nomb, dir):
        self.nombre = nomb
        self.direccion = dir
with app.app_context():
    db.create_all()

class Lugar_EstrategicoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre','direccion')  