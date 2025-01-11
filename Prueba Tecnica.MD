Desarrollador Junior

    • Objetivo: Evaluar conocimientos en POO, persistencia de datos y diseño de aplicaciones
    interactivas.

    • Prueba:

        Sistema de Gestión de Inventarios
            - Diseña un programa que permita:

                1. Registrar productos con atributos como nombre, categoría, cantidad y
                precio.
                2. Buscar productos por categoría o nombre.
                3. Actualizar la cantidad de un producto.
                4. Guardar y cargar datos en un archivo (JSON o base de datos SQLite).

        Requisitos Técnicos:

            - Utiliza programación orientada a objetos.
            - Implementa un menú interactivo con opciones claras para el usuario.
            - Maneja validaciones para entradas incorrectas.

    • Entrega: Código funcional con documentación básica (README).

    • Duración Estimada: 1-2 días.

    • Criterios de Evaluación:

        o Correcto uso de POO y persistencia de datos.
        o Facilidad de uso y claridad del menú interactivo.
        o Robustez del sistema frente a errores

**Solucion:**
    Desarrolle la prueba tecnica con python y su framework Flask, ademas de usar TailwindCSS en las vistas y un poco de JavaScript basico. desarrolle
    el sistema de gestión de inventarios con las siguientes funcionalidades:
        - Crear, leer, actualizar, eliminar y buscar (**CRUD**) productos con atributos como nombre, categoría y precio.
        - Crear, leer, actualizar y eliminar (**CRUD**) categorias
    Utilizando la flexibilidad que me proporciona el framework Flask cree una aplicacion bajo la arquitectura de software MVC apoyandome asimismo de la
    programacion orientada a objetos (**POO**).
    - Para la persistencia de datos utilice la base de datos SQLite.
    - Muestro mensajes informativos faciles de entender para el usuario usando flash
    - Utilice un **menú interactivo** con opciones **claras** para el usuario.
    - Maneje validaciones para entradas incorrectas.
    - Tome el tiempo suficiente para disenar una interfaz limpia y facil de digerir para cualquier usuario del software web.
**Ejecucion**

- Verifica que las dependencias esten instaladas en el entorno virtual (deberian) accediendo a el con el siguiente comando:

  bash
  source .env\scripts\activate
  Luego
  pip install -r requirements.txt

- Ya puedes ejecutar el proyecto con:

  bash
  python app.py
