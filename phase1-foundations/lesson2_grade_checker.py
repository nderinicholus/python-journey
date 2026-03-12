# 1. Creates a list of students, each a dictionary with `name` and `score` (out of 100)
# 2. Has a function `check_grade(score)` that returns a grade:
#     - 80 and above → `"A"`
#     - 60 - 79 → `"B"`
#     - 40 - 59 → `"C"`
#     - Below 40 → `"F"`
# 3. Has a function `show_results(students)` that loops through all students and prints each name, score, and grade

# students = ["Nick", "Brian", "Mary", "Tom"]

students = [
    {"name": "Nick", "score": 85},
    {"name": "Brian", "score": 57},
    {"name": "Mary", "score": 72},
    {"name": "Tom", "score": 35}
]


def check_grade(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "F"


def show_results(students):
    print("=== Student Results ===")
    for student in students:
        name = student["name"]
        score = student["score"]
        grade = check_grade(score)

        print(f"{name:<10} Score: {score}, Grade: {grade}")

show_results(students)
