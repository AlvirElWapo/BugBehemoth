from models.exts import db
from sqlalchemy.orm import relationship

class Departamento(db.Model):
    __tablename__ = 'departamentos'

    id_departamento =  db.Column('id_departamento', db.Integer(), primary_key=True)
    nombre = db.Column('nombre', db.String(255), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)
    updatesd = db.Column('updatesd', db.Date(), nullable=True)

    def __repr__(self):
        return f"<Departamento {self.id_departamento}>"
    
    def serialize(self):
        return{
            'id_departamento': self.id_departamento,
            'nombre': self.nombre,
            'estatus': self.estatus,
            'updatesd': self.updatesd,
            'user': self.user.serialize() if self.user else None,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self):
        
        db.session.commit()