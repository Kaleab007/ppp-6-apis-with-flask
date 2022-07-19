from flask import Blueprint, request
from .import model
show_bp = Blueprint (
    'show',
    __name__,
    ur_prefix='/reptiles/<int:id>'
),
@show_bp.route('/')
def show(id):
    reptile = model.Reptile.query.filter_by(id=id).first()
    reptile_dict = {
        'common_name': reptile.common_name,
        'scientific_name': reptile.scientific_name,
        'conservation_status': reptile.scientific_name,
        'native_habitat': reptile.native_habitat,
        'fun_fact':reptile.fun_fact
    }