from flask import Flask, render_template, request, flash # importar render_template para usar templates
from config import Config                                # importar la configuración de la base de datos   
from models import db, ContactMessage                    # importar el modelo ContactMessage y la instancia db
from datetime import datetime, timedelta                 # importar datetime y timedelta para manejar fechas


app = Flask(__name__)
app.config.from_object(Config)

# Inicializar SQLAlchemy
db.init_app(app)

# Crear tablas al inicio
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html", titulo="SPORT MAX", mensaje="SPORTMAX BEST ENTRETAINMENT")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

# Agrega esta función junto con las otras rutas
@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        correo = request.form.get("correo", "").strip()
        celular = request.form.get("celular", "").strip()
        edad = request.form.get("edad", "").strip()
        mensaje = request.form.get("mensaje", "").strip()

        # Validar que todos los campos obligatorios estén presentes
        if not nombre or not correo or not celular or not edad or not mensaje:
            flash("Todos los campos son obligatorios.", "danger")
            return render_template("contacto.html", enviado=False)
        
        # Validar y convertir celular
        celular_int = None
        try:
            celular_int = int(celular)
            if len(celular) != 10 or not (3000000000 <= celular_int <= 3999999999):
                flash("El celular debe tener 10 dígitos y comenzar con 3.", "danger")
                return render_template("contacto.html", enviado=False)
        except ValueError:
            flash("El celular debe ser un número válido.", "danger")
            return render_template("contacto.html", enviado=False)

        # Validar y convertir edad
        edad_int = None
        try:
            edad_int = int(edad)
            if not (1 <= edad_int <= 120):
                flash("La edad debe estar entre 1 y 120 años.", "danger")
                return render_template("contacto.html", enviado=False)
        except ValueError:
            flash("La edad debe ser un número válido.", "danger")
            return render_template("contacto.html", enviado=False)

        try:
            nuevo = ContactMessage(nombre=nombre, correo=correo, celular=celular_int, edad=edad_int, mensaje=mensaje)
            db.session.add(nuevo)
            db.session.commit()
            return render_template("contacto.html", enviado=True, nombre=nombre)
        except Exception as e:
            db.session.rollback()
            flash("Ocurrió un error guardando el mensaje. Inténtalo nuevamente.", "danger")
            return render_template("contacto.html", enviado=False)

    return render_template("contacto.html", enviado=False)


@app.route("/admin/contactos")
def admin_contactos():
    # --- Parámetros de filtro (GET) ---
    q = request.args.get("q", "", type=str).strip()               # correo (substring)
    date_from_str = request.args.get("from", "", type=str).strip() # YYYY-MM-DD
    date_to_str = request.args.get("to", "", type=str).strip()     # YYYY-MM-DD

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = ContactMessage.query

    # Filtro por correo (contiene)
    if q:
        query = query.filter(ContactMessage.correo.ilike(f"%{q}%"))

    # Filtro por fechas (incluyente)
    date_from = None
    date_to = None
    try:
        if date_from_str:
            date_from = datetime.strptime(date_from_str, "%Y-%m-%d")
            query = query.filter(ContactMessage.created_at >= date_from)
        if date_to_str:
            # incluir todo el día to (23:59:59.999999)
            date_to = datetime.strptime(date_to_str, "%Y-%m-%d") + timedelta(days=1) - timedelta(microseconds=1)
            query = query.filter(ContactMessage.created_at <= date_to)
    except ValueError:
        # Si viene una fecha malformada, no rompe; podrías hacer flash() si quieres
        pass

    query = query.order_by(ContactMessage.created_at.desc())

    # Paginación
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    items = pagination.items

    return render_template(
        "admin_contactos.html",
        items=items,
        pagination=pagination,
        q=q,
        date_from=date_from_str,
        date_to=date_to_str,
        per_page=per_page
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
