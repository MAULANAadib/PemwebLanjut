from flask import jsonify, request
from models.LevelModel import Level
from config import db

##### Level #####
# Level routes
def get_levels():
    levels = Level.query.all()
    return jsonify([level.to_dict() for level in levels])

#Get a single level by id
def get_level(id):
    level = Level.query.get(id)
    if not level:
        return jsonify({'message': 'Level tidak ditemukan'}), 404
    return jsonify(level.to_dict())

#Add a new level
def add_level():
    new_level_data = request.get_json() 
    new_level = Level(
        name=new_level_data['name']
    )
    db.session.add(new_level)
    db.session.commit()
    return jsonify({'message': 'Level added successfully!', 'level': new_level.to_dict()}), 201

#Update a level (PUT)
def update_level(id):
    level = Level.query.get(id)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    
    update_level = request.get_json()
    level.name = update_level.get('name', level.name)

    db.session.commit()
    return jsonify({'message': 'Level updated successfully!', 'level': level.to_dict()})

#Delete a level(DELETE)
def delete_level(id):
    level = Level.query.get(id)
    if not level:
        return jsonify({'message': 'Level tidak ditemukan'}), 404
    
    db.session.delete(level)
    db.session.commit()
    return jsonify({'message': 'Level deleted successfully!'})
