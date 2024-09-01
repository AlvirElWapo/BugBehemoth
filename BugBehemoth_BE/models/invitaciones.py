from models.exts import db
from sqlalchemy.orm import relationship
from datetime import datetime
from models.eventos import Eventos
from models.user import User

class Invitaciones(db.Model):
    __tablename__ = 'invitaciones'

    id = db.Column('id', db.Integer(), primary_key=True)
    id_evento = db.Column('id_evento', db.Integer(), db.ForeignKey('eventos.id_evento'), nullable=False)
    id_invitado = db.Column('id_invitado', db.Integer, db.ForeignKey('users.id_user'), nullable=False)
    created = db.Column('created', db.DateTime(), default=datetime.now())
    updated = db.Column('updated', db.DateTime(), default=datetime.now())

    evento = relationship(Eventos, backref="invitacionesEvento")
    user = relationship(User, backref="invitacionesUser")

    def __repr__(self):
        return f"<Invitaciones {self.id}>"
    
    def serialize(self):
        return{
            'id': self.id,
            'id_evento': self.id_evento,
            'id_invitado': self.id_invitado,
            'created': self.created,
            'updated': self.updated,
            'evento': self.evento.serialize() if self.evento else None,
            'user': self.user.serialize() if self.user else None,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def upadte(self, id_evento, id_invitado):
        self.id_evento = id_evento
        self.id_invitado = id_invitado

        db.session.commit()