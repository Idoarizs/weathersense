from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from app.db.models import db

# Initialize Flask
app = Flask(__name__)
app.config.from_object('app.config.Config')

# Initialize Database, JWT, ORM
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Initialize Route
# app.reigster_blueprint(user, url_prefix='api/v1/auth')
# app.reigster_blueprint(classification, url_prefix='/api/v1/model')

if __name__ == "__main__":
    app.run(debug=True)