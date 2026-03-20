import json
from filter_by_age import filter_users_by_age
from filter_by_email import filter_users_by_email


def filter_users_by_name(name):
    """
    Filter and print users whose name matches
     the search string.
    """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if
        user["name"].lower() == name.lower()
    ]

    if not filtered_users:
        print(f"No users found with name: {name}")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    """Prompt the user for a filter option and the corresponding search term."""
    print("Available filters: name, age, email")
    filter_option = input("What would you like to filter by? ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid number for the age.")

    elif filter_option == "email":
        prefix_to_search = input("Enter the part before the @: ").strip()
        filter_users_by_email(prefix_to_search)

    else:
        print(f"Option '{filter_option}' is not supported.")
