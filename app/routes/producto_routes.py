from flask import Blueprint, flash, render_template, request, jsonify, redirect,url_for
from app.models import Producto
from app.models import Categoria
from app import db

bp = Blueprint('producto', __name__)

@bp.route('/', methods=["GET"])
def index():
    if request.method=="GET":
        productos = db.session.query(Producto, Categoria).join(Categoria, Producto.categoria_id == Categoria.idCategoria).order_by(Producto.idProducto.desc()).all()
        categorias = Categoria.query.all()
        return render_template('index.html', producto=productos, categoria=categorias)

@bp.route('/accion_producto', methods=["POST"])
def accion():
    action = request.form.get('action')
    idProducto = request.form.get("idProducto")
    nombreProducto = request.form.get("nombreProducto")
    categoriaProducto = request.form.get('categoriaProducto')
    precioProducto = request.form.get("precioProducto")

    if action == 'create':
        if not nombreProducto or not categoriaProducto or not precioProducto:
            flash('Por favor llene todos los campos', 'error')
            return redirect(url_for('producto.index'))
        producto_existente = Producto.query.filter_by(nombreProducto=nombreProducto).first()
        if producto_existente:
            flash('El producto ya existe', 'error')
            return redirect(url_for('producto.index'))
        producto = Producto(nombreProducto=nombreProducto, categoria_id=categoriaProducto, precioProducto=precioProducto)
        try:
            db.session.add(producto)
            db.session.commit()
            flash('Producto creado correctamente', 'success')
            return redirect(url_for('producto.index'))
        except Exception  as e:
            flash(f'Error al crear el producto: {str(e)}', 'error')
            return redirect(url_for('producto.index'))

    elif action == 'update':
        if not idProducto or not nombreProducto or not categoriaProducto or not precioProducto:
            flash('Por favor llene todos los campos', 'error')
            return redirect(url_for('producto.index'))
        producto = Producto.query.get(idProducto)
        producto.nombreProducto = nombreProducto
        producto.categoria_id = categoriaProducto
        producto.precioProducto = precioProducto
        try:
            db.session.commit()
            flash('Producto actualizado correctamente', 'success')
            return redirect(url_for('producto.index'))
        except Exception as e:
            flash(f'Error al actualizar el producto: {str(e)}', 'error')
            return redirect(url_for('producto.index'))

    elif action == 'delete':
        if not idProducto:
            flash('Producto no encontrado', 'error')
            return redirect(url_for('producto.index'))
        producto = Producto.query.get(idProducto)
        try:
            db.session.delete(producto)
            db.session.commit()
            flash('Producto eliminado correctamente', 'success')
            return redirect(url_for('producto.index'))
        except Exception as e:
            flash(f'Error al eliminar el producto: {str(e)}', 'error')
            return redirect(url_for('producto.index'))

    return redirect(url_for('producto.index'))

