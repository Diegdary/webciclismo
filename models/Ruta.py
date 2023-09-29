from config.db import app, db, ma

class Usuario(db.Model):
    __tablename__ = "tblruta"

    id = db.Column(db.Integer, primary_key = True)
    id_alerta = db.Column(db.Integer, db.ForeignKey('tblalerta.id'))
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    descripcion_ruta = db.Column(db.String(50))
    nombre_ruta = db.Column(db.String(50))
    ciclovia_inicial = db.Column(db.String(50))
    ciclovia_final = db.Column(db.String(50))
    

    def __init__(self,a,b,c,d,f,g):
        self.id = i
        self.id_usuario = id_usu
        self.mensaje = mens
with app.app_context():
    db.create_all()

class RutaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_usuario','mensaje')