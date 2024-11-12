from flask import jsonify, request
from models.UserModel import User
from models.LevelModel import Level
from config import db

##### USER #####
#GET all USer
def get_users():
    users = User.query.all()
    users_with_levels = []

    for user in users:
        #Ambil level terkait dari book
        level = Level.query.get(user.level_id)

        #
        users_with_levels.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'level_name': level.name if level else "No Level"
        })

    response = {
        'status': 'success',
        'data': {
            'users': users_with_levels
        },
        'message': 'Users retrieved successfully'
    }
    return jsonify(response), 200

#Get a single user by with level name(GET)
def get_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    
    #Ambil level terkait dari user
    level = Level.query.get(user.level_id)
    #Jika level tidak ditemukan, maka level_name akan menjadi "No Level"
    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'level_name': level.name if level else "No Level"

    }
    response = {
        'status': 'success',
        'data': {
            'user': user_data
        },
        'message': 'User retrieved successfully'
    }

    return jsonify(response), 200

#Add a new user (POST)
def add_user():
    new_user_data = request.get_json()
    new_user = User(
        username=new_user_data['username'],
        email=new_user_data['email'],
        level_id=new_user_data['level_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!', 'user': new_user.to_dict()}), 201

#Update a user(PUT)
def update_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    
    update_user = request.get_json()
    user.username = update_user.get('username', user.username)
    user.email = update_user.get('email', user.email)
    user.level_id = update_user.get('level_id', user.level_id)

    db.session.commit()
    return jsonify({'message': 'User updated successfully!', 'user': user.to_dict()})

#Partially update a user (PATCH)
def patch_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    
    update_data = request.get_json()

    #Perbarui hanya jika data tersebut diberikan
    if 'username' in update_data:
        user.username = update_data['username']
    if 'email' in update_data:
        user.email = update_data['email']
    if 'level' in update_data:
        #Pastikan level ada sebelum update
        level = Level.query.get(update_data['level_id'])
        if level:
            user.level_id = update_data['level_id']
        else:
            return jsonify({'message': 'Level tidak ditemukan'}), 404
        
    db.session.commit()
    return jsonify({'message': 'User updated successfully!', 'user': user.to_dict()})

#Delete a user(DELETE)
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'message': 'User tidak ditemukan'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})
