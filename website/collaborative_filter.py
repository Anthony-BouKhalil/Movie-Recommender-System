import math

def main(selected_movies, ratings, movies):
    matrix, user_ratings = create_matrix(selected_movies, ratings, movies)
    averages, user_scores_index = calculate_average(matrix, user_ratings)
    similarity_scores = calculate_similarity_scores(matrix, user_ratings, averages, user_scores_index)

    #I will use positive sim scores (> 0.1)

    """
    Make into helper functions
    """
    # TODO:
        # Generate a results file for the user similarity matrix (can print to a .txt file as a matrix)
        # Mention all from imported data, none from my own user input
    # TODO:
    # Similarity_scores = [0 for i in range(943)]
    # Calculate the similarity score between the user and each user in the matrix (data set)

    # If similarity score (Pearson correlation coefficient) is greater than 0.5 or 0 (see what works better), 
    # matrix user scores will be used
    
    # After all users have been compared
    # Then for every movie the user hasn't seen
    # compute the (score = weighted sum) for the user and all the positive correlation user scores

    # Return the movies with the top 3 highest scores (try other top K values) that have a score greater than 3.5 (test this num with others maybe)

    return None

def create_matrix(selected_movies, ratings, movies):
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
    
    user_ratings = []

    # User Scores
    # movies[:1] because the first movie is 'Please Pick a Movie'
    for movie in movies[1:]:
        if movie in selected_movies:
            user_ratings.append(ratings[selected_movies.index(movie)])
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

    return matrix, user_ratings


def calculate_average(matrix, user_ratings):
    averages = [0 for i in range(943)]
    user_scores_index = []

    for i, score in enumerate(user_ratings):
        if score != 'None':
            user_scores_index.append(i)

    for i, user in enumerate(matrix):
        counter = 0
        for j, score in enumerate(user):
            # No user ratings gave a score of 0, dataset is ratings from 1 to 5
            if score != 0 and j in user_scores_index:
                averages[i] += int(score)
                counter += 1
        if counter > 0:
            averages[i] = averages[i] / counter
    
    return averages, user_scores_index


def calculate_similarity_scores(matrix, user_ratings, averages, user_scores_index):
    numerator = 0
    denominator = 0
    similarity_scores = [0 for i in range(943)]

    for i, user in enumerate(matrix):
        counter = 0
        for j, score in enumerate(user):
            # No user ratings gave a score of 0, dataset is ratings from 1 to 5
            if score != 0 and j in user_scores_index:
                counter += 1
                numerator += (int(score) - averages[i]) * (int(user_ratings[j]) - averages[i])
                denominator += math.sqrt(math.pow(int(score) - averages[i], 2)) * math.sqrt(math.pow(int(user_ratings[j]) - averages[i], 2))
        try:
            similarity_scores[i] = numerator / denominator
        except ZeroDivisionError:
            similarity_scores[i] = 0


    print(sorted(similarity_scores, reverse=True))
    return similarity_scores



def calculate_weighted_sum_rating(matrix, similarity_scores):
    pass
