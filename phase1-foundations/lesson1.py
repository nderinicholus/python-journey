# Dictionaries
# user = {
#   "name": "Nick",
#   "age": 44,
#   "city": "Nairobi"
# }
# print(user["name"])  # Output: Nick
# print(user.get("email", "Not found"))  # Output: Not found

# Lists
# fruits = ["apple", "banana", "mango"]
# print(fruits[0])  # Output: apple
# fruits.append("grape")
# print(fruits)  # Output: ['apple', 'banana', 'mango', '

# if Statements
# age = 10
# if age >= 18:
#     print("You are an adult.")
# elif age >= 13:
#     print("You are a teenager.")
# else:
#     print("You are not a minor.")

# Loops
# fruits = ["apple", "banana", "mango", "grape", "orange"]
# for fruit in fruits:
#     print(fruit)

# Loops with range
# for i in range(5):
#     print(i)  # Output: 0, 1, 2, 3, 4

# for i in range(1, 6):
#     print(i)  # Output: 1, 2, 3, 4, 5

# Functions
# def greet(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# # print(greet("Nick"))  # Output: Hello, Nick!
# print(greet("Nick", "Hi"))  # Output: Hi, Nick!

user = {
    "name": "Nick",
    "age": 44,
    "city": "Nairobi",
    "skills": ["Python", "JavaScript", "SQL"]
}


def show_profile(user):
  print(f"Name: {user['name']}")
  print(f"Age: {user['age']}")
  print(f"City: {user['city']}")
  print("Skills:")
  for skill in user["skills"]:
    print(f" - {skill}")


show_profile(user)


students = [
    {"name": "Nick", "score": 85},
    {"name": "Brian", "score": 57},
    {"name": "Mary", "score": 72},
    {"name": "Tom", "score": 35},
]


def check_grade(score):
    if score >= 80 and score <= 90:
        return "A"

    if score >= 60 and score <= 79:
        return "B"

    if score >= 40 and score <= 59:
        return "C"

    if score < 40:
        return "F"


def show_results(students):
    for student in students:
        name = student["name"]
        score = student["score"]
        grade = check_grade(score)

        print(f"{name}, | Score: {score}, | Grade: {grade}")


show_results(students)
