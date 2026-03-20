import json

def filter_users_by_age(age):
    """Filter and print users from users.json matching the specified age."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age]

    if not filtered_users:
        print(f"No users found with age {age}.")
    else:
        for user in filtered_users:
            print(user)