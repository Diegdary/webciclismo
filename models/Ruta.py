from config.db import app, db, ma

class Usuario(db.Model):
    __tablename__ = "tblruta"

    id = db.Column(db.Integer, primary_key = True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(''))
    mensaje = db.Column(db.String(50))
    

    def __init__(self, i, id_usu, mens):
        self.id = i
        self.id_usuario = id_usu
        self.mensaje = mens
with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario','mensaje')