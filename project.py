from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Movie

app = Flask(__name__)

engine = create_engine('sqlite:///dvdcatalogue.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


# ADD JSON ENDPOINT HERE
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)

@app.route('/')
@app.route('/dashboard/')
def catalogDashboard():
    movies = session.query(Movie).all()
    return render_template('dashboard.html', movies = movies)

@app.route('/movies/create', methods=['GET', 'POST'])
def createNewMovies():
    if request.method == 'POST':
        newMovie = Movie(name=request.form['name'],
                        movie_poster=request.form['movie_poster'],
                        description=request.form['description'],
                        category=request.form['category'])
        session.add(newMovie)
        flash('New Movie %s Successfully Created' % newMovie.name)
        session.commit()
        return redirect(url_for('catalogueDashboard'))
    else:
        return render_template('newMovie.html')


@app.route('/movies/<int:movie_id>/edit', methods=['GET', 'POST'])
def editMovies(movie_id):
    editedMovie = session.query(Movie).filter_by(id=movie_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedMovie.name = request.form['name']
            editedMovie.description = request.form['description']
            editedMovie.movie_poster = request.form['movie_poster']
            editedMovie.category = request.form['category']
            flash('Movie Successfully Edited %s' % editedMovie.name)
            session.commit()
            return redirect(url_for('catalogueDashboard'))
    else:
        return render_template('editMovie.html', movie = editedMovie)


@app.route('/movies/<int:movie_id>/delete', methods=['GET', 'POST'])
def deleteMovies(movie_id):
    movieToDelete = session.query(Movie).filter_by(id=movie_id).one()
    if request.method == 'POST':
        session.delete(movieToDelete)
        flash('%s Successfully Deleted' % movieToDelete.name)
        session.commit()
        return redirect(url_for('catalogueDashboard'))
    else:
        return render_template('deleteMovie.html', movie = movieToDelete.name)

@app.route('/movies/<string:category>')
def showCategoryMovies(category):
    movies = session.query(Movie).filter_by(category=category).all()
    return render_template('category_dashboard.html', movies = movies)

@app.route('/movies/<string:category>/<int:movies_id>')
def showMoviePage(category, movie_id):
    movie = session.query(Movie).filter_by(id=movie_id).one()
    return render_template('movie_dashboard.html', movie = movie)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
