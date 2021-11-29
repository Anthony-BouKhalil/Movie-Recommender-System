from flask import Blueprint, render_template, request, flash
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
        output = []
        
        for i in range(20):
            selected_movies.append(request.form['movie' + str(i)])	

        for i in range(20):
            ratings.append(request.form['rating' + str(i)])	

        for i in range(20):
            if selected_movies[i] == "Please Pick a Movie" and ratings[i] != "Haven't Seen":
                flash('If a rating is picked, it needs a corresponding rating!', category='error')
                return render_template("movies.html", user=current_user, movies=movies)
            elif selected_movies[i] != "Please Pick a Movie" and ratings[i] == "Haven't Seen":
                flash('If a movie is picked, it needs a corresponding movie!', category='error')
                return render_template("movies.html", user=current_user, movies=movies)
        
        for i in range(20):
            inputs.append("You gave " + selected_movies[i] + " a score of " + ratings[i])
        
        results = cf.main(selected_movies, ratings, movies)

        if results != None:
            for i in range(3):
                output.append(results[i] + " is recommended for you because based on your inputs we believe you would give it a score of " + str(round(results[i+3], 2)) + " out of 5")

        if len(output) == 0:
            output.append("No recommendations found")

        return render_template("movies.html", user=current_user, movies=movies, selected_movies=selected_movies, ratings=ratings, \
            inputs=inputs, results=results, output=output)
    
    else:
        return render_template("movies.html", user=current_user, movies=movies)