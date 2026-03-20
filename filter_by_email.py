import json

def filter_users_by_email(prefix):
    """Filter and print users whose email prefix matches the given string."""
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users
        if user.get("email", "").split("@")[0].lower() == prefix.lower()
    ]

    if not filtered_users:
        print(f"No users found with email prefix: {prefix}")
    else:
        for user in filtered_users:
            print(user)