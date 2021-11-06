def create_matrix(scores):
    matrix = [[0 for c in range(len(scores))] for r in range(26)]

    f = open("dataset.txt", "r")
    rows = f.readlines()
    
    for x, row in enumerate(rows):
        row = row.strip().split()
        for y, element in enumerate(row):
            if x != 0 or x != 1 or y != 0:
                matrix[x-2][y-1] = element
    print(matrix)
    return scores
