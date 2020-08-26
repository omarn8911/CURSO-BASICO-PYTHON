# -*- coding: utf-8 -*-
#Generando HTML dinámico

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hola():
	return ("Hola mundo!!!!!!!!!!")
