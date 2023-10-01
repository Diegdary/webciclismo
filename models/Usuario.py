from config.db import app, db, ma

class Usuario(db.Model):
    __tablename__ = "tblusuario"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    password = db.Column(db.String(50))
    genero = db.Column(db.String(50))

    def __init__(self, nombre, correo, password, genero):
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.genero = genero
with app.app_context():
    db.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre','correo','password','genero')