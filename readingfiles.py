import csv

nine = []
ten = []
eleven = []
twelve = []
all = []
with open("datasets/favorite_colors.csv", "r") as f:
    data = csv.DictReader(f)
    for row in data:
        if row["grade"] == "9":
            nine.append(row["favorite_color"])
        if row["grade"] == "10":
            ten.append(row["favorite_color"])
        if row["grade"] == "11":
            eleven.append(row["favorite_color"])
        if row["grade"] == "12":
            twelve.append(row["favorite_color"])

all = nine + ten + eleven + twelve
nine_dict = {"red" : nine.count("red"), "blue" : nine.count("blue"),  "yellow": nine.count("yellow")}
ten_dict = {"red" : ten.count("red"), "blue" : ten.count("blue"),  "yellow": ten.count("yellow")}
eleven_dict = {"red" : eleven.count("red"), "blue" : eleven.count("blue"),  "yellow": eleven.count("yellow")}
twelve_dict = {"red" : twelve.count("red"), "blue" : twelve.count("blue"),  "yellow": twelve.count("yellow")}
all_dict = {"red" : all.count("red"), "blue" : all.count("blue"), "yellow" : all.count("yellow")}
dict = {"nine": nine_dict, "ten": ten_dict, "eleven": eleven_dict, "twelve": twelve_dict, "total" : all_dict}
print(dict)

