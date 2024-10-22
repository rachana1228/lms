# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    db.init_app(app)

    with app.app_context():
        # Import models here to avoid circular imports
        from models import User  # Import your models here

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)