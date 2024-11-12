from flask import Blueprint
from controllers.UserController import get_users, get_user, add_user, patch_user, delete_user, update_user

user_bp = Blueprint('User_bp', __name__)

#Routes for Get all User
user_bp.route('/api/users', methods=['GET'])(get_users)

#Routes for Get a single user (GET)
user_bp.route('/api/users/<int:id>', methods=['GET'])(get_user)

#Routes for Add a new user (POST)
user_bp.route('/api/users', methods=['POST'])(add_user)

#Routes for Update a user(PUT)
user_bp.route('/api/users/<int:id>', methods=['PUT'])(update_user)

#Routes for partially update a user (PATCH)
user_bp.route('/api/users/<int:id>', methods=['PATCH'])(patch_user)

#ROutes for Delete a user (DELETE)
user_bp.route('/api/users/<int:id>', methods=['DELETE'])(delete_user)
