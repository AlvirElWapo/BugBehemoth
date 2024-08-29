from models.exts import db
from models.roles import Role
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id_user = db.Column('id_user', db.Integer(), primary_key=True)
    username = db.Column('username', db.String(50), nullable=False)
    password = db.Column('password', db.String(255), nullable=False)
    email = db.Column('email', db.String(50),  nullable=False)
    nombre = db.Column('nombre', db.String(50), nullable=False)
    id_rol = db.Column('id_rol', db.Integer(), db.ForeignKey('roles.id_rol'), nullable=False)

    role = relationship(Role, backref="roluser")

    def __repr__(self):
        return f"<Role {self.id_user}>"
    
    def serialize(self):
        return{
            'id_user': self.id_user,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'nombre': self.nombre,
            'rol': self.role.serialize() if self.role else None,
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        #codigo para eliminar
        return
    
    def update(self, username, email, nombre, id_rol):
        self.username = username
        self.email = email
        self.nombre = nombre
        self.id_rol = id_rol
        db.session.commit()

    def updatePass(self, password):
        self.password = password
        db.session.commit()
