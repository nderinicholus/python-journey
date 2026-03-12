# Write a Python script that:
# 1. Stores a user's `name`, `age`, `city`, and a list of their `skills`
# 2. Has a function called `show_profile` that takes the user and prints everything neatly
# 3. Calls the function


user = {
    "name": "Nick",
    "age": 44,
    "city": "Nairobi",
    "skills": ["Python", "PHP", "Javascript"]
}


def show_profile(user):
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"City: {user['city']}")
    print("Skills:")
    for skill in user["skills"]:
        print(f" - {skill}")


show_profile(user)
