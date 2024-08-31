from models.exts import db
from sqlalchemy.orm import relationship
from datetime import datetime
from models.recursos import Recursos
from models.tareas import Tareas

class RecursosTarea(db.Model):
    __tablename__ = 'recursos_tarea'

    id_asignacion = db.Column('id_asignacion', db.Integer(), primary_key=True)
    id_recurso = db.Column('id_recurso', db.Integer(), db.ForeignKey('recursos.id_recurso'), nullable=False)
    id_tarea = db.Column('id_tarea', db.Integer(),  db.ForeignKey('tareas.id_tarea'), nullable=False)
    cantidad = db.Column('cantidad', db.Integer(), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)
    created = db.Column('created', db.DateTime(), default=datetime.now)
    updated = db.Column('updated', db.DateTime(), default=datetime.now)


    recurso = relationship(Recursos, backref="recursosRecursosTareas")
    tarea = relationship(Tareas, backref="tareaRecursosTareas")

    def __repr__(self):
        return f"<RecursosTarea {self.id_asignacion}>"
    
    def serialize(self):
        return{
            'id_asignacion': self.id_asignacion,
            'id_recurso': self.id_recurso,
            'id_tarea': self.id_tarea,
            'cantidad': self.cantidad,
            'estatus': self.estatus,
            'created': self.created,
            'updated': self.updated,
            'recurso': self.recurso.serialize() if self.recurso else None,
            'tarea': self.tarea.serialize() if self.tarea else None,
        }
    
    def save(self):
        self.estatus = 0
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, id_tarea, estatus):
        self.updated = datetime.now()
        self.id_tarea = id_tarea
        self.estatus = estatus

        db.session.commit()
    
    def updateStock(self, cantidad):
        self.cantidad = cantidad
        
        db.session.commit()