from flask import Blueprint, request
from app.controllers.accommodation_controller import get_accommodation, details_accommodation

accommodation_bp = Blueprint('accommodation', __name__)

@accommodation_bp.route('/acomodacoes', methods=['GET'])
def accommodation():
  city = request.args.get('cidade')
  return get_accommodation(city)

@accommodation_bp.route('/acomodacoes/<int:id>', methods=['GET'])
def get_accommodation_details(id):
  return details_accommodation(id)
