from models.exts import db
from sqlalchemy.orm import relationship
from models.proyectos import Proyecto
from models.user import User
from datetime import datetime

class Tareas(db.Model):
    __tablename__ = 'Tareas'

    id_tarea = db.Column('id_tarea', db.Integer(), primary_key=True)
    id_proyecto = db.Column('id_proyecto', db.Integer(), db.ForeignKey('proyectos.id_proyecto'), nullable=False)
    responsable = db.Column('responsable', db.Integer(), db.ForeignKey('users.id_user'), nullable=False)
    descripcion = db.Column('descripcion', db.String(), nullable=False)
    estado = db.Column('estado', db.Boolean(), nullable=False)
    created = db.Column('created', db.Date(), default=datetime.now())
    updated = db.Column('updated', db.Date(), default=datetime.now())

    proyecto = relationship(Proyecto, backref="proectosTareas")
    user = relationship(User, backref="userTares")

    def __repr__(self):
        return f"<Tareas {self.id_tarea}>"
    
    def serialize(self):
        return{
            'id_tarea': self.id_tarea,
            'id_proyecto': self.id_proyecto,
            'responsable': self.responsable,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'created': self.created,
            'updated': self.updated,
            'proyecto': self.proyecto.serialize() if self.proyecto else None,
            'user': self.user.serialize() if self.user else None,
        }
    
    def save(self):
        self.estado = 0 
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def upadte(self, id_proyecto, responsable, descripcion):
        self.updated = datetime.now()
        self.id_proyecto = id_proyecto
        self.responsable = responsable
        self.descripcion = descripcion

        db.session.commit()
