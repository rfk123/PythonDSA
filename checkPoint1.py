
def valid_palindrome(s: str) -> bool:
    """
    ignore all non-alphanumeric characters and capitalization when determining whether or not the input string is a volid palindrome
    """
    left = 0
    right = len(s) - 1
    while left < right:
        while not s[right].isalnum():
            right -= 1
        while not s[left].isalnum():
            left += 1
        if s[left].lower() != s[right].lower():
            return False
        right -= 1
        left += 1
    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                      # False
print(valid_palindrome(" "))                               # True


def majority_element(nums: list[int]) -> int:
    """
    Return the value that appears more than n // 2 times
    """
    frequencies = {}
    majority_element = nums[0]
    line = len(nums) // 2
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1
        if frequencies[num] > line:
            majority_element = num
    return majority_element


print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2


def character_replacement(s: str, k: int) -> int:
    """
    you may replace k characters to factor into the longest length
    """
    window = {}
    left = 0
    right = 0
    max_freq = 0
    max_length = 0
    while right < len(s):
        window[s[right]] = window.get(s[right], 0) + 1
        max_freq = max(max_freq, window[s[right]])
        while (right - left + 1) - max_freq > k:
            window[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


print(character_replacement("ABAB", 2))      # 4
print(character_replacement("AABABBA", 1))   # 4)


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = []
    for i in range(len(nums)):
        left = i - 1
        right = i + 1
        product_without = 1
        while left >= 0 or right < len(nums):
            if left >= 0:
                product_without *= nums[left]
                left -= 1
            if right < len(nums):
                product_without *= nums[right]
                right += 1
        result.append(product_without)
    return result


print(product_except_self([0, 2, 10]))

# """ What info do I need to store? Maybe an array of prefix products?
# What pattern/structure fits? I'll need an array
# What does each pointer/variable represent?
# What makes the current state valid?
# What is the time complexity? O(k) + O(m) k is length of unique_t and m is length of unique_s
# What is the space complexity? O(k) k being length of unique_t
# """


"""
One sentence naming the pattern: Performing a set comparison on two strings for a match in distinct characters.
The code: see below
Time and space complexity. Time complexity is O(k) where k is length of unique_t. Space complexity is O(k) + O(m) k being unique_t length and m being unique_s length.
One manual dry run: Done while speaking outloud
"""


def same_unique_characters(s: str, t: str) -> bool:
    """
    Return True when s and t contain the same distinct characters.
    Frequencies do not matter.
    """
    unique_s = set(s)
    unique_t = set(t)

    if len(unique_s) != len(unique_t):
        return False

    for char in unique_t:
        if char not in unique_s:
            return False

    return True


print(same_unique_characters("aab", "abb"))


"""
1. Which system(s) act as clients and which act as servers?
So the customer's CRM data (client side) will be sent via HTTP to the enrichment provider (server side)
2. Roughly what HTTP request would you expect to make to the enrichment provider?
Think about method, endpoint, headers and possibly parameters/body.
So a request includes a method, url, header(s), and body. 
method: GET (because we want to receive information and not alter anything)
url: /companies
headers: maybe content-type and authorization (to describe that what we are sending is JSON and that we are authorized to send this)
body:
{
company_name: "Borant Corp",
}

3. What would you expect the enrichment provider to return?
Well the enrichment provider will enrich the pre-existing data that the client already has so maybe some body like:
{
company_name: "Borant Corp",
employee_count: 508,
corupt: True,
}
4. Once you receive that response, what needs to happen to get the information back into the CRM?
I imagine that we need to verify the data being returned, perform some business logic, transform the data in some way, write to a db, then
put the company back into the CRM (I dont really know what CRM means)
5. What are some things you can already imagine going wrong?
There are plenty of things that could go wrong such as: wrong auth token, wrong route url, mismatched body data type with header content-type, 
we could be unaware with what the enrichment provider api returns and expect the wrong thing, etc.
"""
