from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Store(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    owner = db.Column(db.String(150), nullable=False)
    year_stablished = db.Column(db.Integer, nullable=False)
    number_employees = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Store('{self.name}', '{self.location}', '{self.owner}', '{self.year_stablished}', '{self.number_employees}')"