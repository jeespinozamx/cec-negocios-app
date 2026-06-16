from flask import Flask, render_template
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(override=True)

app= Flask(__name__)
engine = create_engine(os.environ.get('STRING_CONEXION'))



@app.route("/login")
def login():
    query= text('SELECT * FROM negocios')
    with engine.connect() as connection:
        result= connection.execute(query)
        for row in result:
            print(row) 
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