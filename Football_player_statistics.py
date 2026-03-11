goals = {
    "Jin": 8,
    "Leo": 5,
    "Tom": 6
}

for player, goal in goals.items():
    print(player, goal)

sorted_players = sorted(goals.items(), key=lambda x: x[1], reverse=True)   

for players1, goal1 in sorted_players:
    print(players1, goal1)