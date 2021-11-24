movies = []
# Reading movies
f = open("u.item", "r", encoding = "ISO-8859-1")
rows = f.readlines()
for row in rows:
    row = row.split("|")
    movies.append(row[1])
f.close()

matrix = [[0 for c in range(len(movies))] for r in range(943)]
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

with open("user_similarity_matrix.txt", 'w') as f:
    f.write("\t" + "Movies" + "\n")
    with open("u.item", "r", encoding = "ISO-8859-1") as f1:
        lines = f1.readlines()
        for line in lines:
            line = line.split("|")
            f.write("\t" + line[1].ljust(81, " ") + "\t")
    f1.close()
    f.write("\n")
    for i, user in enumerate(matrix):
        f.write(str(i) + "\t")
        for j, score in enumerate(user):
            f.write(str(score).ljust(81, " ") + "\t"*2)
        f.write("\n")
f.close()