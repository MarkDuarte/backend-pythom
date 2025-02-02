from flask import Flask
from flask_cors import CORS

def create_app():
  app = Flask(__name__)

  CORS(app)

  from app.routes.accommodation import accommodation_bp
  app.register_blueprint(accommodation_bp)
  
  return app