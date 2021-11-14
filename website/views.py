from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import collaborative_filter as cf

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def movies():
    movies = [] 
    movies.append("Please Pick a Movie")
    # Reading movies
    f = open("u.item", "r", encoding = "ISO-8859-1")
    rows = f.readlines()
    for row in rows:
        row = row.split("|")
        movies.append(row[1])
    f.close()

    if request.method == 'POST':
        selected_movies = []
        ratings = []
        inputs = []
        
        for i in range(10):
            selected_movies.append(request.form['movie' + str(i)])	

        for i in range(10):
            ratings.append(request.form['rating' + str(i)])	

        for i in range(10):
            inputs.append("You gave " + selected_movies[i] + " a score of " + ratings[i])
        

        results = cf.main(selected_movies, ratings, movies)
        return render_template("movies.html", user=current_user, movies=movies, selected_movies=selected_movies, ratings=ratings, \
            inputs=inputs, results=results)
    
    else:
        return render_template("movies.html", user=current_user, movies=movies)
