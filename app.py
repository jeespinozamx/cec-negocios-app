from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(override=True)

app= Flask(__name__)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registro")
def registro():
    return render_template("registro-usuario.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/negocios")
def negocios():
    return render_template("negocios.html")

@app.route("/crear-negocio")
def crear_negocio():
    return render_template("crear-negocio.html")

@app.route("/actualizar-negocio")
def actualizar_negocio():
    return render_template("actualizar-negocio.html")

@app.route("/ver-negocio")
def ver_negocio():
    return render_template("ver-negocio.html")

if __name__=="__main__":
    app.run()