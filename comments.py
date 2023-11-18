from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    responses = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')

    def __repr__(self):
        return f'<Comment {self.author}, {self.message}, {self.rating}>'

def setup_database():
    with app.app_context():
        # Create the database and tables
        db.create_all()

        # To add a new comment
        new_comment = Comment(author='User1', message='This is a message', rating=5)
        db.session.add(new_comment)
        db.session.commit()

        # To respond to a comment
        response = Comment(author='User2', message='This is a response', rating=4, parent_id=new_comment.id)
        db.session.add(response)
        db.session.commit()

if __name__ == '__main__':
    setup_database()
