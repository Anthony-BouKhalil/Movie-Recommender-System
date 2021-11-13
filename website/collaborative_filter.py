import math

def create_matrix(selected_movie, ratings, movies):
    """
    TODO:
    Add code in view.py for 
    @views.route('/', methods=['GET', 'POST'])
    @login_required
    def movies():
    if request.method == 'POST':
    Put ratings in a set, if only 2 inputs, do not allow (flash error category msg) will result in Division by zero
    Can just say to the user, "Not all ratings can be the same"
    Another Case: "You need to rate at least 2 movies"
    I may need to check to see if the movie & rating combo is filled (if one is changed, the other should be as well) 
        -specifically at least 2 ratings should be filled but they should also have movies picked (that are unique) 
    """
    # len(movies)-1 because the first movie is 'Please Pick a Movie'
    matrix = [[0 for c in range(len(movies)-1)] for r in range(943)]
    similarity_scores = [0 for i in range(943)]
    user_ratings = []

    # User Scores
    # movies[:1] because the first movie is 'Please Pick a Movie'
    for movie in movies[1:]:
        if movie in selected_movie:
            user_ratings.append(ratings[selected_movie.index(movie)])
        else:
            user_ratings.append('None')

    # Reading dataset
    f = open("u.data", "r", encoding = "ISO-8859-1")
    lines = f.readlines()
    for line in lines:
        # user id | item id | rating | timestamp
        line = line.split()
        # int(line[0])-1 because the index of the movies row in matrix starts at 0
        movie = int(line[0])-1
        # int(line[1])-1 because the index of the user column in matrix starts at 0
        user_id = int(line[1])-1
        user_rating = int(line[2])
        matrix[movie][user_id] = user_rating
    f.close()

    """
    Make into helper functions
    """
    # TODO:
        # Generate a results file for the user similarity matrix (can print to a .txt file as a matrix)
        # Mention all from imported data, none from my own user input
    # TODO:
    # Calculate the average for user and each user in the matrix (data set) with only the movies that the have both rated
    # Calculate the similarity score between the user and each user in the matrix (data set)

    # If similarity score (Pearson correlation coefficient) is greater than 0.5 or 0 (see what works better), 
    # matrix user scores will be used
    
    # After all users have been compared
    # Then for every movie the user hasn't seen
    # compute the (score = weighted sum) for the user and all the positive correlation user scores

    # Return the movies with the top 3 highest scores (try other top K values) that have a score greater than 3.5 (test this num with others maybe)


    return None