from models.exts import db
from datetime import datetime
from sqlalchemy.orm import relationship
from models.user import User

class Proyecto(db.Model):
    __tablename__ = 'proyectos'

    id_proyecto = db.Column('id_proyecto', db.Integer(), primary_key=True)
    nombre = db.Column('nombre', db.String(255), nullable=False)
    id_user_director = db.Column('id_user_director', db.Integer(), db.ForeignKey('users.id_user'), nullable=False)
    fecha_creado = db.Column('fecha_creado', db.DateTime(), default=datetime.now())
    fecha_expira = db.Column('fecha_expira', db.Date(), nullable=False)
    descripcion = db.Column('descripcion', db.String(255), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)
    updatesd = db.Column('updatesd', db.DateTime(), default=datetime.now())

    user = relationship(User,backref="usersProyectos")

    def __repr__(self):
        return f"<Proyecto {self.id_proyecto}>"
    
    def serialize(self):
        return{
            'id_proyecto':self.id_proyecto,
            'nombre':self.nombre,
            'id_user_director': self.id_user_director,
            'fecha_creado': self.fecha_creado,
            'fecha_expira': self.fecha_expira,
            'descripcion': self.descripcion,
            'updatesd': self.updatesd,
            'user': self.user.serialize() if self.user else None,
        }
    
    def save(self):
        self.estatus = 0
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, nombre, fecha_expira, descripcion):
        self.updatesd = datetime.now()
        self.nombre = nombre
        self.fecha_expira = fecha_expira
        self.descripcion = descripcion

        db.session.commit()