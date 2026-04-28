#Start!!
players = [
    {"name": "Keshav", "level": 10},
    {"name": "Zoro", "level": 5}
]

# 2. Add New Data
print("--- ADD PLAYER ---")
new_name = input("Enter name: ")
new_lvl = int(input("Enter level: "))

new_p = {"name": new_name, "level": new_lvl}
players.append(new_p)

# 3. View and Check Data
print("--- CHECK PLAYER ---")
index = int(input("Enter index (0, 1, or 2): "))

if index < len(players):
    target = players[index]
    print("Player:", target["name"])
    
    if target["level"] > 9:
        print("Rank: Pro Player")
    else:
        print("Rank: Noob")
else:
    print("Error: Player not found!")
