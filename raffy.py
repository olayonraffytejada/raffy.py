player_x = 0
player_y = 0
treasure_x = 5
treasure_y = 3

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while True:
    move = input("Enter move (up/down/left/right): ").lower()

    if move == "up":
        player_y += 1
    elif move == "down":
        player_y -= 1
    elif move == "left":
        player_x -= 1
    elif move == "right":
        player_x += 1
    else:
        print("Invalid move! Try again.")
        continue

    print(f"You are now at ({player_x}, {player_y})")

    if player_x == treasure_x and player_y == treasure_y:
        print(" Congrats you found the treasure! Game over!")
        break
