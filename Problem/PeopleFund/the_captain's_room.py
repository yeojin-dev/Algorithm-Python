_ = input()
rooms = input().split()
family_rooms = set()
captain_rooms = set()

for room in rooms:
    if room in captain_rooms:
        family_rooms.add(room)
    else:
        captain_rooms.add(room)

print((captain_rooms-family_rooms).pop())
