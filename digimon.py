# Henry Greenhut
# 10/25/22

"""
What is the average speed (Spd) of all Digimon?

Write a function that can count the number of Digimon with a specific attribute. 
For example, count_digimon("Type", "Vaccine") would return 70.

The Digimon on your team are restricted by the total amount of Memory that they need. 
If your team only has 15 Memory, name a team of up to 3 Digimon that has at least 300 attack (Atk) in total.

Describe your process in finding these answers. 
Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better,
 and what you learned during this lab. Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response!
 """

import csv
# Open file and cast to a list so it can be reused
with open("datasets/digimon.csv", "r") as f:
    data = csv.DictReader(f)
    data = list(data)

# Loop through file to find the total # of rows and the total speed
# Then divide total speed by # of rows to get average speed
def get_average_speed():
    speed = {"Count": 0, "Total Speed": 0}
    for row in data:
        speed["Count"] += 1
        speed["Total Speed"] += int(row["Spd"])
    averageSpeed = round(speed["Total Speed"]/speed["Count"], 3)
    return "The average speed is " + str(averageSpeed)

# Loop through file, counting the matching columns with matching attributes.
def count_digimon(column, attribute):
    count = 0
    for row in data:
        if row[column] == attribute:
            count += 1
    return str(count) + " digimon with the " + str(column) + " " + str(attribute)

# Function used to sort list
# https://www.geeksforgeeks.org/sort-in-python/
def attack_per_memory(elem):
    return elem[0]/elem[1]

def assemble_team(max_memory, min_attack):
    atk = []
    for row in data:
        # Only include rows that aren't over the max memory
        if int(row["Memory"]) <= int(max_memory):
            # Checks for rows that satisfy constraints alone
            if int(row["Atk"]) >= int(min_attack):
                return "Digimon " + row["Number"] + " with " + row["Atk"] + " attack and " + row["Memory"] + " memory"
            atk.append([int(row["Atk"]), int(row["Memory"]), int(row["Number"])])
# Sort list by most attack per memory to make the algorithm more likely to find a matching row faster.
    atk.sort(key = attack_per_memory, reverse=True)
    # Use nested for loops to find a group of three rows that fits the constraints.
    for i in range(len(atk)):
        for j in range(len(atk)):
            for k in range(len(atk)):
                if i != j and j != k and i != k:
                    if (atk[i][0] + atk[j][0] + atk[k][0] >= min_attack) and (atk[i][1] + atk[j][1] + atk[k][1] <= max_memory):
                        return ("Digimon " + 
                        str(atk[i][2]) + " " + str(atk[j][2]) + " " + str(atk[k][2]) + 
                        " with " + str(atk[i][0] + atk[j][0] + atk[k][0]) + 
                        " total attack and " + str(atk[i][1] + atk[j][1] + atk[k][1])
                         + " total memory")


print(get_average_speed())

print(count_digimon("Type", "Vaccine"))

print(assemble_team(15, 300))
print(assemble_team(15, 400))
print(assemble_team(5, 100))
            










