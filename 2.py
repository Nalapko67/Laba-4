grade_map = {
    "unsatisfactory": 2,
    "satisfactory": 3,
    "good": 4,
    "excellent": 5
}

students = [
    {"name": "Ivanenko", "math": 3, "physics": 4, "num_methods": 2},
    {"name": "Petrenko", "math": 4, "physics": 2, "num_methods": 4},
    {"name": "Sydorenko", "math": 5, "physics": 3, "num_methods": 4},
    {"name": "Kruk", "math": 5, "physics": 5, "num_methods": 5},
    {"name": "Hlub", "math": 3, "physics": 4, "num_methods": 4}
]

subjects = ["math", "physics", "num_methods"]
subject_names = {
    "math": "Higher Math",
    "physics": "Physics",
    "num_methods": "Numerical Methods"
}

subject_averages = {}

for subject in subjects:
    total = sum(student[subject] for student in students)
    subject_averages[subject] = total / len(students)

print(f"{'Subject':<20}{'Average Grade':<15}")
print("-" * 35)

for subject, avg in subject_averages.items():
    print(f"{subject_names[subject]:<20}{avg:<15.2f}")