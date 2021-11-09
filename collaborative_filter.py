import math
import copy

def create_matrix(user_scores):
    matrix = [[0 for c in range(len(user_scores))] for r in range(26)]
    cosine_similarity_scores = [0 for i in range(26)]

    # Reading dataset
    f = open("dataset.txt", "r")
    rows = f.readlines()
    
    for x, row in enumerate(rows):
        row = row.strip().split()
        for y, element in enumerate(row):
            if x != 0 or x != 1 or y != 0:
                matrix[x-2][y-1] = element
    
    row_mean_matrix = copy.deepcopy(matrix)
    row_mean_user_scores = copy.deepcopy(user_scores)

    # Normalize ratings by subtracting mean rating for each user in dataset
    for x, row in enumerate(matrix):
        accumulator = 0
        counter = 0
        for y, element in enumerate(row):
            if element == '_':
                pass
            else:
                matrix[x][y] = int(element)
                accumulator += matrix[x][y]
                counter += 1

        for y, element in enumerate(row):
            if element == '_':
                row_mean_matrix[x][y] = 0
            else:
                row_mean_matrix[x][y] = int(element) - accumulator/counter
            
    # Normalize ratings by subtracting mean rating for current user ratings
    accumulator = 0
    counter = 0
    for x, score in enumerate(row_mean_user_scores):
        if score != 'None':
            accumulator += int(row_mean_user_scores[x])
            counter += 1

    for x, score in enumerate(row_mean_user_scores):
        if score == 'None':
            row_mean_user_scores[x] = 0
        else:
            row_mean_user_scores[x] = int(score) - accumulator/counter

    # Cosine Similarity Scores:
    for i in range (26):
        cosine_similarity_scores[i] = cosine_similarity(row_mean_user_scores, row_mean_matrix[i], user_scores, matrix[i])
    print(cosine_similarity_scores)
    return list(map(str, cosine_similarity_scores))
    

def cosine_similarity(row_mean_user_scores, row_mean_matrix, user_scores, matrix):
    # Mean rating for cosine similarity score
    try:
        numerator = 0
        for x, score in enumerate(row_mean_user_scores):
            numerator += score * row_mean_matrix[x]

        user_scores_length = math.sqrt(sum([number ** 2 for number in row_mean_user_scores]))
        dataset_scores_length = math.sqrt(sum([number ** 2 for number in row_mean_matrix]))

        score = (numerator) / (user_scores_length * dataset_scores_length)
        return score
    # If all the user ratings are the same, mean rating will result in ZeroDivisionError
    # Use regular ratings instead
    except ZeroDivisionError:
        print(user_scores)
        print(matrix)
        numerator = 0
        for x, score in enumerate(matrix):
            if type(matrix[x]) == int:
                numerator += score * matrix[x]

        user_scores_length = math.sqrt(sum([int(number) ** 2 for number in user_scores if number != 'None']))
        dataset_scores_length = math.sqrt(sum([number ** 2 for number in matrix if type(number) == int]))

        score = (numerator) / (user_scores_length * dataset_scores_length)
        return score
        
