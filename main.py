from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

db = SQLAlchemy(app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    actors = db.Column(db.String(150), nullable=False)
    publicationyear = db.Column(db.String(50), nullable=False)


def create_db():
    with app.app_context():
        db.create_all()


# create the routes
@app.route('/')
def movies():
    users = User.query.all()
    return render_template('movies.html', users=users)


@app.route('/add-movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        actors = request.form['actors']
        publicationyear = request.form['publication year']

        add_movie = movies(title=title, genre=genre,
                        actors=actors, publicationyear=publicationyear)
        db.session.add(Add_movie)
        db.session.commit()
        return redirect(url_for('movies'))
    return render_template('add-movie.html', title='add a movie')


if __name__ == '__main__':
    create_db()
    app.run(port=5001,debug=True)
