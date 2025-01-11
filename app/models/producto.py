from app import db

class Producto(db.Model):
    __tablename__='producto'
    idProducto = db.Column(db.Integer, primary_key=True, nullable=False)
    nombreProducto = db.Column(db.String(100), nullable=False)
    precioProducto = db.Column(db.Float, nullable=False)

    #llave foranea de la tabla categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.idCategoria', ondelete='CASCADE'), nullable=False)
    #relacion con la tabla categoria
    categoria = db.relationship('Categoria', backref=db.backref('producto', lazy=True))

    def __repr__(self):
        return f'<Producto {self.nombreProducto}>'