# data_types.py

# 1. Inputs: int and float
user_name = input("Enter name: ")
rank = int(input("Enter rank number: "))
win_rate = float(input("Enter win rate: "))

# 2. Collections: List, Tuple, and Set
skills = ["Python", "Gaming", "Editing"]
coordinates = (27.7, 85.3)
tags = {"Tech", "AI", "Code", "Tech"}

# 3. Dictionary
profile = {
    "name": user_name,
    "rank": rank,
    "rate": win_rate,
    "skills": skills
}

# 4. Output (using commas)
print("Profile Name:", profile["name"])
print("Rank:", profile["rank"])
print("Win Rate Percentage:", profile["rate"])
print("Skill List:", skills)
print("Fixed Data:", coordinates)
print("Unique Tags:", tags)
