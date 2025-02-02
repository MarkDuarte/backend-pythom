import json
from flask import jsonify

def loading_accommodation():
  with open('app/data/accommodation.json') as file:
    data = json.load(file)
  return data

def get_accommodation(city=None):
  accommodation = loading_accommodation()
  if city:
    accommodation = [a for a in accommodation if a['cidade'].lower() == city.lower()]
  return jsonify(accommodation)

def details_accommodation(id):
  accommodation = loading_accommodation()
  accommodation = next((a for a in accommodation if a['id'] == id), None)
  if accommodation:
    return jsonify(accommodation)
  else:
    return jsonify({'message': 'Accommodation not found'}), 404