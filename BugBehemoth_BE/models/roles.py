from models.exts import db

class Role(db.Model):
    __tablename__ = 'roles'

    id_rol = db.Column('id_rol', db.Integer(), primary_key=True)
    rol = db.Column('rol', db.String(50), nullable=False)
    estatus = db.Column('estatus', db.Boolean(), nullable=False)

    def __repr__(self):
        return f"<Role {self.rol}>"
    
    def serialize(self):
        return {
            'id_rol': self.id_rol,
            'rol': self.rol,
            'estatus': self.estatus
        }
    
    def save(self):
        self.estatus = 1
        db.session.add(self)
        db.session.commit()

    def delete(self):
        self.estatus = 0
        db.session.commit()

    def update(self, rol, estatus):
        self.rol = rol
        self.estatus = estatus
        
        db.session.commit()
