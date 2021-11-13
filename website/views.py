from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

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
        scores = []
        ratings = []
        scores.append(request.form['movie0'])
        scores.append(request.form['movie1'])
        scores.append(request.form['movie2'])
        scores.append(request.form['movie3'])
        scores.append(request.form['movie4'])
        scores.append(request.form['movie5'])
        scores.append(request.form['movie6'])
        scores.append(request.form['movie7'])
        scores.append(request.form['movie8'])
        scores.append(request.form['movie9'])

        ratings.append(request.form['rating0'])
        ratings.append(request.form['rating1'])
        ratings.append(request.form['rating2'])
        ratings.append(request.form['rating3'])
        ratings.append(request.form['rating4'])
        ratings.append(request.form['rating5'])
        ratings.append(request.form['rating6'])
        ratings.append(request.form['rating7'])
        ratings.append(request.form['rating8'])
        ratings.append(request.form['rating9'])
        print(scores)
        print(ratings)
        return render_template("movies.html", user=current_user, movies=movies, scores=scores)
    
    else:
        return render_template("movies.html", user=current_user, movies=movies)
