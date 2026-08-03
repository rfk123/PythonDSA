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


"""
