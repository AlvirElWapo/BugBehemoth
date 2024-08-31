from models.exts import db
from datetime import datetime
from sqlalchemy.orm import relationship
from models.user import User

class Alertas(db.Model):
    __tablename__ = 'alertas'

    id_alerta = db.Column('id_alerta', db.Integer(), primary_key=True)
    destinatario = db.Column('destinatario', db.Integer(), db.ForeignKey('users.id_user'), nullable=False)
    fecha_alerta = db.Column('fecha_alerta',db.Date(), nullable=False)
    tipo = db.Column('tipo', db.Integer(), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)
    created = db.Column('created', db.Date(), default=datetime.now())
    updated = db.Column('updated', db.Date(), default=datetime.now())

    user = relationship(User,backref="alertasUser")

    def __repr__(self):
        return f"<Alertas {self.id_alerta}>"
    
    def serialize(self):
        return{
            'id_alerta': self.id_alerta,
            'destinatario': self.destinatario,
            'fecha_alerta': self.fecha_alerta,
            'tipo': self.tipo,
            'estatus': self.estatus,
            'created': self.created,
            'updated': self.updated,
            'user': self.user.serialize() if self.user else None,
        }
    
    def save(self):
        self.estatus = 0
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, estatus):
        self.estatus = estatus
        self.update = datetime.now()

        db.session.commit()