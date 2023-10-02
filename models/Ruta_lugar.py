from config.db import app, db, ma

class Ruta_lugar(db.Model):
    __tablename__ = "tblruta_lugar"

    id = db.Column(db.Integer, primary_key = True)
    id_ruta = db.Column(db.Integer, db.ForeignKey('tblruta.id'))
    id_lugar = db.Column(db.Integer, db.ForeignKey('tbllugar_estrategico.id'))

    def __init__(self, id_ruta, id_lugar):
        self.id_ruta = id_ruta
        self.id_lugar = id_lugar
with app.app_context():
    db.create_all()

class Ruta_lugarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_ruta','id_lugar')