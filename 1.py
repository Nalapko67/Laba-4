students = [
    {"id": 1, "name": "Ivanchuk S.O.", "grades": [4, 3, 3, 4]},
    {"id": 2, "name": "Panchenko I.A.", "grades": [5, 4, 4, 5]},
    {"id": 3, "name": "Zaiets O.M.", "grades": [3, 4, 4, 4]},
    {"id": 4, "name": "Velbytskyi P.O.", "grades": [4, 3, 3, 3]},
    {"id": 5, "name": "Sydorenko V.R.", "grades": [2, 3, 3, 2]},
    {"id": 6, "name": "Kravchenko Z.I.", "grades": [3, 5, 4, 5]},
    {"id": 7, "name": "Yakubiv R.N.", "grades": [5, 4, 4, 3]},
    {"id": 8, "name": "Zorenko P.M.", "grades": [4, 2, 3, 3]},
    {"id": 9, "name": "Berestyak G.S.", "grades": [4, 5, 5, 5]},
    {"id": 10, "name": "Dyachyk N.S.", "grades": [5, 5, 4, 4]}
]

print(f"{'No.':<5}{'Surname':<20}{'CS':<6}{'Math':<6}{'Phys':<6}{'Prog':<6}")
print("-" * 49)

filtered_count = 0

for student in students:
    if 3 in student["grades"]:
        filtered_count += 1
        g = student["grades"]
        print(f"{student['id']:<5}{student['name']:<20}{g[0]:<6}{g[1]:<6}{g[2]:<6}{g[3]:<6}")

print("-" * 49)
print(f"Total students with at least one grade '3': {filtered_count}")