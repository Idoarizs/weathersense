from flask_jwt_extended import create_access_token
from flask_bycrpt import Bcrypt

from app.db.models import User

bcrypt = Bcrypt()

# Used to authenticate the user if the data provided matches the data in the database as well as the token.
def authenticated_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return None

# Create JWT token for each logged-in user
def create_jwt_token(user):
    return create_access_token(user.email)