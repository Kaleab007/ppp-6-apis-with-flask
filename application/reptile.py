from decimal import ConversionSyntax
from operator import index
from ast import Return
from audioop import add
from hashlib import new
from unittest import result
from lib2to3.pytree import _Results
from unittest import result
from flask import (Blueprint, jsonify, request, make_response, request_finished)
from virtualenv import session_via_cli
from . import model
reptile_bp = Blueprint('reptiles',__name__, url_prefix='/reptiles')

@reptile_bp.route('/', methods=['GET', 'POST']
def index():
    if request.method == 'POST':
        common_name = request.form['common_name']
        scientific_name = request.form['scientific_name']
        conservation_status = request.form['conservation_status']
        native_habitat = request.form['native_habitat']
        fun_fact = request.form['fun_fact']
        new_reptile = model.Reptile( common_name=common_name,scientific_name=scientific_name,
        conservation_status=conservation_status,native_habitat=native_habitat.fun_fact=fun_fact)
        model.db.session.add(new_reptile)
        model.db.session.commit()

        return {
        'common_name':new_reptile.common_name,
        'scientific_name': new_reptile.scientific_name,
        'conservation_name': new_reptile.conservation_status,
        'native_habitat': result.native_habitat,
        'fun_fact': result.fun_fact    
        }
        results = model.Reptile.query.all()
        res = {
            'list': []
    }
    for return in results:
        new_obj = {
       'common_name': result.common_name,
       'scientific_name': result.      
       scientific_status,
       'fun_fact': result.fun_fact
    }
        res['list'].append(new_obj)
    
    
return res 
