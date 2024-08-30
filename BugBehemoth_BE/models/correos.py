from models.exts import db
from models.user import User
from sqlalchemy.orm import relationship
from datetime import datetime

class Correos(db.Model):
    __tablename__ = 'correos'

    id_correo = db.Column('id_correo', db.Integer(), primary_key=True )
    destinatario = db.Column('destinatario', db.Integer(), db.ForeignKey('users.id_user'), nullable=False)
    code_html = db.Column('code_html', db.Text(), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)
    created = db.Column('created', db.Date(), default=datetime.now(), nullable=True)
    updated = db.Column('updated', db.Date(), default=datetime.now(), nullable=True)

    user = relationship(User, backref="userCorreo")

    def __repr__(self):
        return f"<Correos {self.id_correo}>"
    
    def serialize(self):
        return{
            'id_correo': self.id_correo,
            'destinatario': self.destinatario,
            'code_html': self.code_html,
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
    
    def update(self):
        #codigo para actualizar
        db.session.commit()
    
