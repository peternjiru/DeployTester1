from sqlalchemy_serializer import SerializerMixin
from config import db

class Program(db.Model, SerializerMixin):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    grade = db.Column(db.String)
   

    def __repr__(self):
        return f'<Name {self.name} | Grade: {self.grade}>'
