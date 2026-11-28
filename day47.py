

# Continuing on with strings in DSA
s = "unusual"

print(s.removeprefix("un"))  # "usual"
print(s.strip("un"))        # "sual"


def normalize_msg(text: str) -> str:
    if not text:
        return ''
    tokens = text.split()
    cleaned = []
    for token in tokens:
        word = token.strip('.,!?;:').casefold()
        if word:
            cleaned.append(word)
    return ' '.join(cleaned)


"""
In this code, I originally check to see if the text is empty. if it is then we return empty string. Otherwise we continue on by splitting the 
input text on whitespace. I also initialize an empty string to put valid tokens into later (we are asked to remove tokens that are empty after normalization).
I then go through each token in tokens and strip them of beginning and trailing mentioned characters, then I chained the casefold method to that strip method.
if the token is not an empty string then we can append it to the cleaned list. Once the loop is done I use the join method to join all 
of the tokens on a singular whitespace. The space complexity is O(n) and the time complexity is also O(n).
"""

print(normalize_msg("  HELLO,\tWorld!!  "))
print(normalize_msg("Python   IS\nFUN."))
print(normalize_msg("..."))
print(normalize_msg("don't !.? STOP!"))
print(normalize_msg("don't STOP!"))

print(normalize_msg("well-done, indeed."))
print(normalize_msg("Straße, STRASSE"))
print(normalize_msg(""))
"""
Split the input on arbitrary whitespace (including tabs and newlines).

Remove the characters .,!?;: from the beginning and end of each token, but not from the middle.

Convert each remaining token using casefold().

Discard tokens that become empty after stripping punctuation.

Join the remaining tokens using exactly one ordinary space.

"  HELLO,\tWorld!!  "	"hello world"
"Python   IS\nFUN."	"python is fun"
"..."	""
"don't STOP!"	"don't stop"
"well-done, indeed."	"well-done indeed"
"Straße, STRASSE"	"strasse strasse"
""	""
"""
