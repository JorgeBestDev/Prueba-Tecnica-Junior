from app import db

class Categoria(db.Model):
    __tablename__='categoria'
    idCategoria = db.Column(db.Integer, primary_key=True, nullable=False)
    nombreCategoria = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f'<Categoria {self.nombreCategoria}>'