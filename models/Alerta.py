from config.db import app, db, ma

class Alerta(db.Model):
    __tablename__ = "tblalerta"

    id = db.Column(db.Integer, primary_key = True)
    zonas_peligrosas = db.Column(db.String(50))
    intersecciones = db.Column(db.String(50))
    cambio_clima = db.Column(db.String(50))
    fecha_alerta = db.Column(db.Date)

    def __init__(self, zpeligrosas, inter, cambioc, falerta):
        self.zonas_peligrosas = zpeligrosas
        self.intersecciones = inter
        self.cambio_clima = cambioc
        self.fecha_alerta = falerta
with app.app_context():
    db.create_all()

class AlertaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'zonas_peligrosas','intersecciones','cambio_clima','fecha_alerta')  