# Today I will start by going over set rocognition (no code)

"""
Scenario 1: Contains Duplicate
What must be remembered? We need to keep track of all of the values we have come across while iterating through the list. 
Is a set enough? A set will be enouhg for this problem since we can just check if the current value has been seen before (the value will be in our set)
Would a dictionary add useful information? You could technically use a hashmap for this problem and have the key:value pair be number:frequency and just check if frequency is ever 2. But no,
a dictionary is not needed.
What information would a set lose? Using a set for this problem means that we will not be keeping track of indices or frequency counts.

Scenario 2: First Duplicate
What must be remembered? I think that we just need to remember all of the values that we have previously come across (like contains duplicate scenario). So, just the 'seen' values.
Is a set enough? A set will be enough since the first duplicate problem is exactly the same as the contains duplicate problem except that we return the value instead of a boolean value. Set 
is enough because we store the values. Although we can just return the value that our current pointer is on.
Would a dictionary add useful information? A dictionary would not be helpful here because we can get by fine without it. It would just add information that we COULD use but don't NEED to use. 
What information would a set lose? By using a set we forfeit keeping indices or frequency counts as dictionaries would/could include. However, we do not need these things for this. 

Scenario 3: Two Sum
What must be remembered? For this problem, we must keep track of both the value and the index since indices are what we will be returning but values are what we are comparing. Also, for this specific 
problem, we are given a target integer. Whats useful about this is that we can subtract our current value in the list from the target value to check if the difference has been seen previously in the list. 
Is a set enough? A set will not be enough because we will need to remember the indices that belong to each value in our list and sets only contain values and not additional information like indices.
Would a dictionary add useful information? A dictionary would be useful for this problem since we will need to store information (indices) along with our seen values. 
What information would a set lose? A set would not allow for us to store anything like indices or frequency counts. In regard to this problem, we wouldn't be able to efficiently find the index of one of
our values that make up the two sum. 

Scenario 4: Intersection 
What must be remembered? Simply put, we must remember unique values (indices don't matter and frequency counts don't matter)
Is a set enough? A set will be enough because all we have to check is if we have seen a value before. Sets are able to store values without any additional information which is just what we need.
Would a dictionary add useful information? A dictionary would not add useful information since we only need the values.
What information would a set lose? Even though we wont need them, a set will lose us the ability to keep track of indices and frequency counts.

Scenario 5: Neabry Duplicate
What must be remembered? We will need to store values along with their last seen index in order to see if there are duplicate values within k indices of one another.
Is a set enough? A set will not be enough because we will need to store additional information with our values (their last seen index)
Would a dictionary add useful information? Yes, a dictionary would add useful information because in the key:value pair we can frame it as number:index and use that index to determine if the current
value's index is within k of the last seen duplicate value's index.
What information would a set lose? A set would lose us the ability to check the distance between two duplicate values since there will be no additional information stored along with the values.
^^
For the scenario above, a set is actually enough to solve this problem. If we use the combination of a set and a sliding window we can check to see if there a duplicate value in our current window set.
"""


# Now I will practice choosing between a set and a dictionary
"""
Scenario 1: Longest substring without repeating characters
What does the algorithm need to know? Thinking about what the structure shoudl represent at this moment instead of across the entire string, I believe that the algorithm needs to know if there are any
duplicates within the current window. We can answer that by keeping track of values that we have come across before. We will need to remove and add values to our set as our window shrinks/grows.
Could a set work? Yes, a set could work for this problem as we only require keeping track of the current values within the window and no additional information is needed that a set couldnt provide.
Could a dictionary work? Yes, a dictionary could work but that would be for a diffenent soultion where we would shrink our window from the left while there is a key with a value of 2.
Which is simpler, and why? A set is simpler for this problem because it requires storing less information and doing less checks. Each solution would require a sliding window so it just comes down to 
the extra amount of steps and storage.

Scenario 2: Character Replacement
What does the algorithm need to know? The algorithm needs to know these things: the length of the current window, the frequency of the most frequenct char, and the number of substitutions allowed. I 
believe that, in order to find the frequency of the most frequent char in the current window, we need to use a hashmap to store the chars and their frequencies.
Could a set work? A set will not work because it won't allow us to know how many letters need to be substituted to have a valid substring.
Could a dictionary work? Yes, a dictionary will work because we can keep track of the frequency counts of each letter in the current window. You should be able to take the difference between the length 
of the window and the freqeuncy of the most frequent char and have that value be less than or equal to the value k in order for the current window to be valid.
Which is simpler, and why? The dictionary is more simple (only because I am not entirely sure of what the set solution would look like).

Scenario 3: Happy Number
What does the algorithm need to know? I believe that we will need to keep track of numbers that we have seen before in order to determine whether or not we have entered a cycle. This 
will require using a set. 
Could a set work? Yes, a set will work in order to determine whether or not we are in a cycle by letting us know if we have seen a specific value before.
Could a dictionary work? A dictionary could work but it requires storing extra information that we dont necessarily need.
Which is simpler, and why? A set is simpler because we dont need to store any other information other than the values that we have seen.
What information is required to determine a cycle? The set will help determine if we have entered a cycle because as we transform our number over and over again, if the number it transforms to is one we have 
already seen then we know that it will just continuously get back to this point infinetly and therefore dont need to iterate anymore.

Scenario 4: Group Anagrams 
What does the algorithm need to know? The algorithm needs to determine how to group anagrams together. The first step to that is to figure out how to compare words in order to determine that they 
are anagrams and the second thing is we need to find a way to group those words together. How the algorithm will compare words is by creating bucket arrays of length 26(the size of the alphabet) and
each index in the array represents a letter's frequency count. Once we have this frequency array built out, we can convert it into a string and use that string (or tuple) as a key in a dictionary so
that any word that is a match anagram will be placed in the value array of this key.
Could a set work? A set alone would not work because you will need to store more information along with a value.
Could a dictionary work? A dictionary will work for the above reasons. We will have a frequency array act as the key and have a value list where we can group anagram words together.
Which is simpler, and why? A dictionary is simpler because it seems to be the only option.

Scenario 5: Longest Consecutive Sequence
What does the algorithm need to know? The algorithm just needs to know all of the unique values in the input array. This is because we dont need to include duplicates since, for example, when we are at the 
integer 4 we only care about if there is a following 5 anywhere in the input array.
Could a set work? A set will work because we will build out our set of unique values sourced from the input array and iterate through that set only building out a 'window' when we get to an integer
that doesnt have a integer - 1 neighbor (its the starting intger in its sequence). Then we can keep going and compare the current window length to that of the max_length until we no longer have a 
valid window.
Could a dictionary work? A dictionary could work as well but will contain unnecessary information.
Which is simpler, and why? Using a set would be simpler since we only need to remember seen values and not their indices or frequency counts.

"""

"""
Problem A
    Given a list of integers, return the first index where the value has appeared earlier. Return -1 if every value is unique.
What must be remembered? The algorithm must remember values that we have seen before. That way we can determine if the current value is one that has been already seen.
Set, dictionary, pointers, or sliding window? For this problem, I would use a set to store the unique values that we have seen before. 
What does the chosen structure represent? The set just is a memory bank that holds values that we have come across.
What would make the approach valid? Since we traverse the list left to right, the first value that we come across that has been seen before will be our solution and we can return that value. If we dont
ever come across a duplicate value then we can just return -1 after iterating through the list. 

Problem B
Given two strings, determine whether every character in the first string can be matched with an available copy in the second string. Each character in the second string may be used only once.
What must be remembered? The algorithm will need to remember what characters from string1 are tied to what characters in string2 and vise versa. So this may mean that we will require two hashmaps.
Set, dictionary, pointers, or sliding window? I would use a dictionary (two dictionaries) for this problem.
What does the chosen structure represent? The two dictionaries will represent character matches from string1 to string2 and from string2 to string1.
What would make the approach valid? Going through each input string at once we can check to see if the characters are already in a hashmap and if they are, what characters can they map to. This will 
allow us to make validity checks based on if both characters at the ith positions are pointing to right matching character. If not then we can return False, otherwise return True. 

Problem C
Given a sorted list and a target, determine whether two different values add to the target using constant extra space.
What must be remembered? What must be 'remembered' is really nothing except for two pointer indices. 
Set, dictionary, pointers, or sliding window? For this problem, I would use a converging two pointer technique.
What does the chosen structure represent? The chosen structure represents two nums from different sides of the spectrum (one is the lowest num and one is the highest valued num). By taking the sum
of these two values we can determine the movement of our pointers since the input list in sorted. 
What would make the approach valid? What makes this approach valid is that we will either find two values that sum to the target value or the two pointers will overlap and we will know that there
exist no two values in the list that could sum to the target value. Consider two pointers starting on opposite ends of the list. If the sum is larger than the target value then we will shrink inwards
from the right (right pointer -= 1) and then compare those. Otherwise, if the sum was lower than the target value, we would shrink inwards from the left (left pointer += 1).

"""
