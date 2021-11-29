import math
import collections

def main(selected_movies, ratings, movies):
    dictionary = {}
    scores = []
    movie_names = []

    matrix, user_ratings = create_matrix(selected_movies, ratings, movies)
    averages, user_scores_index = calculate_average(matrix, user_ratings)
    similarity_scores = calculate_similarity_scores(matrix, user_ratings, averages, user_scores_index)
    movie_scores = calculate_weighted_sum_rating(matrix, user_scores_index, similarity_scores)

    for i, score in enumerate(movie_scores):
        dictionary[score] = i

    sorted_dictionary = collections.OrderedDict(sorted(dictionary.items(), reverse=True))
    top_three = list(sorted_dictionary.keys())[0:3]

    for top_k in top_three:
        # dictionary[top_k]+1 because movies[0] is 'Please Pick a Movie'
        if top_k != 0:
            scores.append(top_k)
            movie_names.append(movies[dictionary[top_k]+1])
            print(top_k, " ", movies[dictionary[top_k]+1])
        else:
            return None

    return movie_names + scores

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
        movie = int(line[1])-1
        # int(line[1])-1 because the index of the user column in matrix starts at 0
        user_id = int(line[0])-1
        user_rating = int(line[2])
        matrix[user_id][movie] = user_rating
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
        for j, score in enumerate(user):
            # No user ratings gave a score of 0, dataset is ratings from 1 to 5
            if score != 0 and j in user_scores_index:
                numerator += (int(score) - averages[i]) * (int(user_ratings[j]) - averages[i])
                denominator += math.sqrt(math.pow(int(score) - averages[i], 2)) * math.sqrt(math.pow(int(user_ratings[j]) - averages[i], 2))
        try:
            similarity_scores[i] = numerator / denominator
        except ZeroDivisionError:
            similarity_scores[i] = 0


    print(sorted(similarity_scores, reverse=True))
    return similarity_scores


def calculate_weighted_sum_rating(matrix, user_scores_index, similarity_scores):
    numerator = [0 for i in range(1682)]
    movie_scores = [0 for i in range(1682)]
    denominator = [0 for i in range(1682)]


    #Transpose matrix
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for x in range(1682):
        #The user rated that movie, don't want to recommend it
        if x in user_scores_index:
            continue
        for y in range(943):
            if similarity_scores[y] > 0.5:
                numerator[x] += similarity_scores[y] * int(transposed_matrix[x][y]) 
                denominator[x] += similarity_scores[y]
        try:
            movie_scores[x] = numerator[x] / denominator[x]
        except ZeroDivisionError:
            movie_scores[x] = 0

    return movie_scores    