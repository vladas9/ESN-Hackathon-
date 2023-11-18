from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from scrape import main  # Uncomment this if scrape.py is ready

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mainDB.db'
db = SQLAlchemy(app)

class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    icon_link = db.Column(db.String, nullable=True)
    short_description = db.Column(db.String, nullable=True)
    official_website = db.Column(db.String, nullable=True)
    news = db.relationship('News', backref='party', lazy=True)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    post_date = db.Column(db.DateTime, nullable=False)
    theme = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    media_link = db.Column(db.String, nullable=True)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='news', lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    profile_picture = db.Column(db.String, nullable=True)
    short_description = db.Column(db.String, nullable=True)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    comments = db.relationship('Comment', backref='author', lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # The foreign key to create a self-referential relationship
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    # Define the relationship to itself
    responses = db.relationship('Comment', backref=db.backref('parent', remote_side=[id]), lazy=True)


@app.route('/', methods=['GET'])
def add_news_form():
    return render_template('test.html')

@app.route('/add-news', methods=['POST'])
def add_news():
    try:
        # Extract and validate data from form
        party_name = request.form.get('party_name')
        post_date = request.form.get('post_date')
        theme= request.form.get('theme')
        rating = request.form.get('rating')
        media_link = request.form.get('media_link')
        content = request.form.get('content')

        if not all([party_name, post_date, theme, rating, media_link, content]):
            return "Please fill in all fields", 400

        # Convert and validate date and integers
        post_date = datetime.strptime(post_date, '%Y-%m-%d')
        theme = int(theme)
        rating = int(rating)

        # Find or create the party
        party = Party.query.filter_by(name=party_name).first()
        if not party:
            party = Party(name=party_name)
            db.session.add(party)
            db.session.commit()

        # Create and add news item
        news_item = News(party_id=party.id, post_date=post_date, theme=theme, rating=rating, media_link=media_link, content=content)
        db.session.add(news_item)
        db.session.commit()

        return "News added successfully"
    except ValueError as e:
        return f"Invalid input: {e}", 400
    except Exception as e:
        return f"An error occurred: {e}", 500


def update_news_from_scrape():
    try:
        scraped_data = main()  # Call your scraping function
        for item in scraped_data:
            # Process each scraped item (you need to define this process)
            pass
        return "News updated successfully"
    except Exception as e:
        return f"An error occurred: {e}"

from flask_migrate import Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
