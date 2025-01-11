from flask import Blueprint, flash, render_template, request, jsonify, redirect,url_for
from app.models import Producto
from app.models import Categoria
from app import db

bp = Blueprint('categoria', __name__)

@bp.route('/categoria_accion', methods=["POST"])
def accion():
    if request.method == "POST":
        boton = request.form.get('button')
        idCategoria = request.form.get('idCategoria', None)
        nombreCategoria = request.form.get('nombreCategoria', '').strip()

        if boton == 'Delete':
            if not idCategoria:
                flash('El ID de la categoría es requerido para eliminar', 'warning')
                return redirect(url_for('producto.index'))

            categoria = Categoria.query.get(idCategoria)
            if not categoria:
                flash('La categoría no existe', 'error')
                return redirect(url_for('producto.index'))
            try:
                db.session.delete(categoria)
                db.session.commit()
                flash('Categoría eliminada correctamente', 'success')
                return redirect(url_for('producto.index'))
            except :
                flash(f'No puedes eliminar una categoria ligada a mas registros', 'warning')
                return redirect(url_for('producto.index'))

        elif boton == 'Save':
            if not nombreCategoria:
                flash('El nombre de la categoría no puede estar vacío', 'warning')
                return redirect(url_for('producto.index'))

            if idCategoria:
                # Actualizar categoría existente
                categoria = Categoria.query.get(idCategoria)

                # Verificar si el nombre ya existe en otra categoría
                categoria_existente = Categoria.query.filter_by(nombreCategoria=nombreCategoria).first()
                if categoria_existente and categoria_existente.id != int(idCategoria):
                    flash('Ya existe otra categoría con este nombre', 'warning')
                    return redirect(url_for('producto.index'))

                categoria.nombreCategoria = nombreCategoria
                try:
                    db.session.commit()
                    flash('Categoría actualizada correctamente', 'success')
                    return redirect(url_for('producto.index'))
                except Exception as e:
                    flash(f'Error al actualizar la categoría {str(e)}', 'error')
                    return redirect(url_for('producto.index'))
            else:
                # Crear nueva categoría
                categoria_existente = Categoria.query.filter_by(nombreCategoria=nombreCategoria).first()
                if categoria_existente:
                    flash('La categoría ya existe', 'warning')
                    return redirect(url_for('producto.index'))

                nueva_categoria = Categoria(nombreCategoria=nombreCategoria)
                try:
                    db.session.add(nueva_categoria)
                    db.session.commit()
                    flash('Categoría creada correctamente', 'success')
                    return redirect(url_for('producto.index'))
                except Exception as e:
                    flash(f'Error al crear la categoría {str(e)}', 'error')
                    return redirect(url_for('producto.index'))

        else:
            flash('Acción no permitida', 'error')
            return redirect(url_for('producto.index'))

    flash('Método HTTP no permitido', 'error')
    return redirect(url_for('producto.index'))
