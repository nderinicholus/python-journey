# CONTROL FLOW & LOGIC
# Logical operators
# ----------------------

# age = 17
# has_id = True

# if age >= 18 and has_id:
#     print("Entry allowed!")

# if age < 18 or not has_id:
#     print("Entry denied!")

# Truthy and Falsy
# ----------------
# skills = ["PHP", "Javascript"]
# if skills:
#     print("Has skills")

# name = ""
# if not name:
#     print("Name is missing")

# Match Statement
# ----------------

# role = "admin"
# match role:
#     case "admin":
#         print("Full access")

#     case "Editor":
#         print("Edit access")

#     case _:
#         print("Read only")

# While loops
# -------------
# count = 1
# while count <= 5:
#     print(f"Count: {count}")
#     count += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5:
        continue
    if num == 8:
        break
    print(num)
