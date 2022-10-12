# Henry Greenhut
# 10/13/22
# Art of Data

import csv
sizes = {}
islands = {}

with open("datasets/penguins.csv", "r") as f:
    data = csv.DictReader(f)
    for row in data:
# If the species is not in the dictionary yet, add it with the count of one and record its first length and mass
# If it is in the dictionary, add to the count and its measurements to eventually find sum of measurements
        if row["bill_length_mm"] != "":
            if row["species"] not in sizes:
                sizes[row["species"]] = {"count": 1, "bill_length" : float(row["bill_length_mm"]), "body_mass": float(row["body_mass_g"])}
            else:
                sizes[row["species"]]["count"] +=1
                sizes[row["species"]]["bill_length"] += float(row["bill_length_mm"])
                sizes[row["species"]]["body_mass"] += float(row["body_mass_g"])

# The count of species per island is split into another dictionary ->
# organized by island and accounting for rows w/ row & species info, but no measurements
        if row["island"] not in islands:
            islands[row["island"]] = {row["species"] : 1}
        elif row["species"] not in islands[row["island"]]:
            islands[row["island"]][row["species"]] = 1
        else:
            islands[row["island"]][row["species"]] += 1
        
averageLength = -1
averageMass = -1
# Loop through species to find highest average by dividing the sum of all measurements by the count 
for i in sizes:
    if sizes[i]["bill_length"]/sizes[i]["count"] > averageLength:
        averageLength = sizes[i]["bill_length"]/sizes[i]["count"]
        longest = i
    if sizes[i]["body_mass"]/sizes[i]["count"] > averageMass:
        averageMass = sizes[i]["body_mass"]/sizes[i]["count"]
        biggest = i

# print(sizes)
print(longest + " is the longest: " + str(int(averageLength)) + " mm on average")
print(biggest + " is the biggest: " + str(int(averageMass)) + " grams on average")

# print(islands)
print("There are " + str(islands["Dream"]["Chinstrap"]) + " Chinstrap penguins on Dream island")



