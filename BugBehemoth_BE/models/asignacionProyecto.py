from models.exts import db
from datetime import datetime
from sqlalchemy.orm import relationship
from models.user import User
from models.proyectos import Proyecto

class AsignacionProyecto(db.Model):
    __tablename__ = 'asignacion_proyectos'

    id_asignacion = db.Column('id_asignacion', db.Integer(), primary_key=True)
    id_user = db.Column('id_user' ,db.Integer(), db.ForeignKey('users.id_user'), nullable=False)
    id_proyecto = db.Column('id_proyecto', db.Integer, db.ForeignKey('proyectos.id_proyecto'), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)
    created = db.Column('created', db.DateTime(), default=datetime.now())
    updated = db.Column('updated', db.DateTime(), default=datetime.now())

    user = relationship(User,backref="asginacionProyectosUsers")
    proyecto = relationship(Proyecto,backref="asginacionProyectosProyecto")

    def __repr__(self):
        return f"<AsignacionProyecto {self.id_asignacion}>"
    
    def serialize(self):
        return{
            'id_asignacion': self.id_asignacion,
            'id_user': self.id_user,
            'id_proyecto': self.id_proyecto,
            'estatus': self.estatus,
            'created': self.created,
            'updated': self.updated,
            'user': self.user.serialize() if self.user else None,
            'proyecto': self.proyecto.serialize() if self.proyecto else None,
        }
    
    def save(self):
        self.estatus = 1
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, id_user, id_proyecto, estatus):
        self.id_user = id_user
        self.id_proyecto = id_proyecto
        self.estatus = estatus

        db.session.commit()