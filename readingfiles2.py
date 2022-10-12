import csv
dict = {}
with open("datasets/favorite_colors.csv", "r") as f:
          data = csv.DictReader(f)
          for col in data.fieldnames:
              for row in data:
                  if row["grade"] == col:
                      print(row["favorite_color"])
                      col = {row["grade"], row["favorite_color"]}
print(col)
