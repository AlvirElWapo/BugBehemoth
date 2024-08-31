from models.exts import db
from sqlalchemy.orm import relationship
from datetime import datetime

class Eventos(db.Model):
    __tablename__ = 'eventos'

    id_evento = db.Column('id_evento', db.Integer(), primary_key=True)
    fecha = db.Column('fecha', db.Date(), nullable=False)
    descripcion = db.Column('descripcion', db.String(255), nullable=False)
    estatus = db.Column('estatus', db.Boolean, nullable=False)
    created = db.Column('created', db.Date(), default=datetime.now())
    updated = db.Column('updated', db.Date(), default=datetime.now())

    def __repr__(self):
        return f"<Eventos {self.id_evento}>"
    
    def serialize(self):
        return{
            'id_evento': self.id_evento,
            'fecha': self.fecha,
            'descripcion': self.descripcion,
            'estatus': self.estatus,
            'created': self.created,
            'updated': self.updated
        }
    
    def save(self):
        self.estatus = 1
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

        db.session.commit()