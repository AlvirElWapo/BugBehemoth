from models.exts import db
from datetime import datetime

class Recursos(db.Model):
    __tablename__ = 'recursos'

    id_recurso = db.Column('id_recurso', db.Integer(), primary_key=True)
    nombre = db.Column('nombre', db.String(255), nullable=False)
    cantidad_total = db.Colum('cantidad_total', db.Integer(),nullable=False)
    cantidad_disponible = db.Column('cantidad_disponible', db.Integer(), nullable=False)
    updated = db.Column('updated', db.Date(), default=datetime.now())

    def __repr__(self):
        return f"<Recursos {self.id_recurso}>"
    
    def serialize(self):
        return{
            'id_recurso': self.id_recurso,
            'nombre': self.nombre,
            'cantidad_total': self.cantidad_total,
            'updated': self.updated
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, nombre, cantidad_total, cantidad_disponible):
        self.updated = datetime.now()
        self.nombre = nombre
        self.cantidad_total = cantidad_total
        self.cantidad_disponible = cantidad_disponible

        db.session.commit()