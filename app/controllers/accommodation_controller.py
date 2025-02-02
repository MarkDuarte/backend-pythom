import json
from flask import jsonify
from app.utils.helpers import remove_accents

def loading_accommodation():
  with open('app/data/accommodation.json') as file:
    data = json.load(file)
  return data

def get_accommodation(city=None):
    accommodation = loading_accommodation()

    if city:
        city_normalized = remove_accents(city.lower())
        accommodation = [
            a for a in accommodation
            if city_normalized in remove_accents(a['cidade'].lower())
        ]

    return jsonify(accommodation)

def details_accommodation(id):
  accommodation = loading_accommodation()
  accommodation = next((a for a in accommodation if a['id'] == id), None)
  if accommodation:
    return jsonify(accommodation)
  else:
    return jsonify({'message': 'Accommodation not found'}), 404