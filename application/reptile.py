from decimal import ConversionSyntax
from operator import index
from flask import (Blueprint, jsonify, request, make_response, request_finished)
from . import model
reptile_bp = Blueprint('reptiles',__name__, url_prefix='/reptiles')

@reptile_bp.route('/', methods=['GET', 'POST']
def index():
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.formm['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']
        new_reptile = model.model.Reptile( common_name+common_name,
        conservation_status=conservation_status,native_habitat=native_habitat.fun_fact=fun_fact)