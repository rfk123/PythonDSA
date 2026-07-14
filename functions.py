
# Functions are just reusable blocks of code that performs specific tasks
location = "Baltimore"


def welcome_message(name: str, greeting="Hello") -> None:
    location = "Maryland"
    print(f"{greeting}, {name} from {location}!")
    print("Hello")


welcome_message("reza", "poopy")
