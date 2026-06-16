from flask import Flask, render_template
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

load_dotenv(override=True)

db= SQLAlchemy()

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('STRING_CONEXION')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

@app.route("/")
def index():
    consulta= text("SELECT * FROM negocios LIMIT 5")
    resultado= db.session.execute(consulta)

    negocios= resultado.mappings().all()
    print(negocios)

    return render_template("index.html", negocios=negocios)

@app.route("/login")
def login():
    return render_template("login.html")

# Equipo 1
@app.route("/registro")
def registro():
    return render_template("registro-usuario.html")

# Equipo 5
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Equipo 4
@app.route("/negocios")
def negocios():
    return render_template("negocios.html")

# Equipo 2
@app.route("/crear-negocio")
def crear_negocio():
    return render_template("crear-negocio.html")

# Equipo 3
@app.route("/actualizar-negocio")
def actualizar_negocio():
    return render_template("actualizar-negocio.html")

# Equipo 6
@app.route("/ver-negocio")
def ver_negocio():
    return render_template("ver-negocio.html")

if __name__=="__main__":
    app.run()