from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = 'owners'
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String , unique = True)
    
    pets = (db.relationship ('Pet' , backref = 'owner'))
    
    def __repr__(self):
        return f'<Pet Owner {self.name}>'
    
    
    
class Pet(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    
    owner_id = db.Column(db.Integer , db.ForeignKey(Owner.id))
    
    def __repr__(self):
        return f'<Pet{self.name} , {self.species}>'