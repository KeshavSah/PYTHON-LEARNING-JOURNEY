# Automatically ranks and prints out a list of my favorite series using a for loop.

my_favorites = ["One Piece", "Solo Leveling", "The Boxer", "Kaoru Hana wa Rin to Saku"]
total_items = len(my_favorites)

print("--- MY TOP RANKINGS ---")

for i in range(total_items):
    rank = i + 1
    current_title = my_favorites[i]
    print("#" + str(rank) + ": " + current_title)

print("-----------------------")
print("Total titles ranked: " + str(total_items))
