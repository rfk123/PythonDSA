

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

# print(normalize_msg("  HELLO,\tWorld!!  "))
# print(normalize_msg("Python   IS\nFUN."))
# print(normalize_msg("..."))
# print(normalize_msg("don't !.? STOP!"))
# print(normalize_msg("don't STOP!"))

# print(normalize_msg("well-done, indeed."))
# print(normalize_msg("Straße, STRASSE"))
# print(normalize_msg(""))
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


def parse_settings(raw: str) -> list[tuple[str, str]]:
    settings = raw.split(';')
    result = []
    for i in range(len(settings)):
        # will return a tuple with three elements
        setting = settings[i].partition('=')
        if setting[1] == '=':
            key = setting[0].strip().casefold()
            if not key:
                continue
            val = setting[2].strip()
            result.append((key, val))
    return result


"""
I was able to determine if a setting is valid by frist checking if parition had a valid split and then checking if the key was not empty after normalization.
If both of those things are true then we have a valid setting to include in our result array. partition handles extra = signs since it 
only splits on the first occurence. This solution is O(n) for both space complexity and time complexity.
"""
print(parse_settings(" User = Ada ; token = a=b=c ; invalid ; =oops ; MODE= fast "))

print(parse_settings("X=1;Y=2"))
print(parse_settings("a=; b = "))
print(parse_settings("hello; world"))
print(parse_settings("x=a=b=c"))
print(parse_settings("a=1;a=2"))


'''
"X=1;Y=2"	[("x", "1"), ("y", "2")]
"a=; b = "	[("a", ""), ("b", "")]
"hello; world"	[]
"x=a=b=c"	[("x", "a=b=c")]
"a=1;a=2"	[("a", "1"), ("a", "2")]
"; ; "	[]
'''
