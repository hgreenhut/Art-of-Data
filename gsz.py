import csv
with open("datasets/favorite_colors.csv", "r") as f:
    data = csv.DictReader(f)
    for row in data:
        print(row)
