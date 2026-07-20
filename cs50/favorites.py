# import csv

# # with open("favorites.csv", "r") as file:
# #     reader = csv.DictReader(file)
# #     for row in reader:
# #         # favorite = row["player_name"]
# #         print(row["player_name"])

# with open("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     # scratch, c, python = 0, 0, 0
#     Spanish, South_Africa, Dutch = 0, 0, 0
#     # for row in reader:
#     #     favorite = row["height_cm"]
#     #     print(favorite)
#     for row in reader:
#         favorite = row["nationality"]
#         if favorite == "Spanish":
#             Spanish += 1
#         elif favorite == "South African":
#             South_Africa += 1
#         elif favorite == "Dutch":
#             Dutch += 1
    
#     print((Spanish, South_Africa, Dutch))

# from cs50 import SQL

# db = SQL("sqlite:///favorites.db")

# favorite = input("Favorite: ")

# rows = db.execute("select count(*) as n from favorites where nationality = ?")
# row = rows[0]

# print(row["n"])