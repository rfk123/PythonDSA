# Today I will start by going over set rocognition (no code)

"""
Scenario 1: Contains Duplicate
What must be remembered? We need to keep track of all of the values we have come across while iterating through the list. 
Is a set enough? A set will be enouhg for this problem since we can just check if the current value has been seen before (the value will be in our set)
Would a dictionary add useful information? You could technically use a hashmap for this problem and have the key:value pair be number:frequency and just check if frequency is ever 2. But no,
a dictionary is not needed.
What information would a set lose? Using a set for this problem means that we will not be keeping track of indices or frequency counts.

Scenario 2: 
What must be remembered? I think that we just need to remember all of the values that we have previously come across (like contains duplicate scenario). So, just the 'seen' values.
Is a set enough? A set will be enough since the first duplicate problem is exactly the same as the contains duplicate problem except that we return the value instead of a boolean value. Set 
is enough because we store the values. Although we can just return the value that our current pointer is on.
Would a dictionary add useful information? A dictionary would not be helpful here because we can get by fine without it. It would just add information that we COULD use but don't NEED to use. 
What information would a set lose? By using a set we forfeit keeping indices or frequency counts as dictionaries would/could include. However, we do not need these things for this. 




"""
