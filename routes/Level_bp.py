from flask import Blueprint
from controllers.LevelController import get_levels, get_level, add_level, update_level, delete_level

level_bp = Blueprint ('Level_bp', __name__)

#Routes for Get all Level
level_bp.route('/api/level', methods=['GET'])(get_levels)

#Routes for Get a single level (GET)
level_bp.route('/api/level/<int:id>', methods=['GET'])(get_level)

#Routes for Add a new level (POST)
level_bp.route('/api/level', methods=['POST'])(add_level)

#Routes for Update a level (PUT)
level_bp.route('/api/level/<int:id>', methods=['PUT'])(update_level)

#Routes for Delete a level (DELETE)
level_bp.route('/api/level/<int:id>', methods=['DELETE'])(delete_level)