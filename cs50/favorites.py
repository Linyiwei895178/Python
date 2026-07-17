import csv

# with open("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # favorite = row["player_name"]
#         print(row["player_name"])

with open("favorites.csv", "r") as file:
    reader = csv.DicReader(file)
    scratch, c, python = 0, 0, 0
    for row in reader:
        favorite = row["language"]
        