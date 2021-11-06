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
    
    row_mean_matrix = matrix
    row_mean_user_scores = user_scores

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

    #Try to use from sklearn.metrics.pairwise import cosine_similarity
    #Implement my own implementation of cosine similarity
    #for score in cosine_similarity_scores:
    #    cosine_similarity_scores[score] = cosine_similarity([row_mean_user_scores], [row_mean_matrix[score]])
    print(row_mean_user_scores)
    return list(map(str, row_mean_user_scores))