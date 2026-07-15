
# Functions are just reusable blocks of code that performs specific tasks
location = "Baltimore"


def welcome_message(name: str, greeting="Hello") -> None:
    location = "Maryland"
    print(f"{greeting}, {name} from {location}!")
    print("Hello")


welcome_message("reza", "poopy")


def longest_without_repeating(word):
    right = 0
    left = 0
    max_length = 0
    seen = {}
    while right < len(word):
        while word[right] in seen:
            seen[word[right]] -= 1
            if seen[word[right]] == 0:
                del seen[word[right]]
            left += 1
        seen[word[right]] = 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


print(longest_without_repeating('startpl'))
