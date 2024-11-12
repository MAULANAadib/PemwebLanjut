from config import db

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    #Relasi dengan User (one-to-many)
    users = db.relationship('User', backref='level', lazy=True)

    def to_dict(self):
        return {
            'id': self.id, 
            'name': self.name
            }