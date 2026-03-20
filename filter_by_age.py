import json


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age]

    if not filtered_users:
        print(f"No users found with age {age}.")
    else:
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (age): ").strip().lower()

    if filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid number for the age.")

    else:
        print("Filtering by that option is not yet supported.")