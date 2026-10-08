"""
1. nums[i]
- what it does / returns -> returns the value in nums at index i
- time complexity -> O(1)
- extra space complexity if relevant -> No
- one-sentence reason -> Quick lookup of what value is being held at index i in array nums
2. nums[i] = x
- what it does / returns -> This updates the value in nums at the ith index to equal x (or to have the reference of x) doesnt return anything
- time complexity -> O(1)
- extra space complexity if relevant -> No
- one-sentence reason -> python arrays maintain their size and capacity values but also the starting address. Using these we can use the index to find the value to update in O(1)
3. nums.append(x)
- what it does / returns -> I believe this returns None but it adds a value to the end of a list
- time complexity -> amortized O(1)
- extra space complexity if relevant -> if you append to an array where the size is == to the capacity then you will need extra space
- one-sentence reason -> it inserts a value at nums.size index 
4. nums.insert(0, x)
- what it does / returns -> I believe this returns none but this specific example inserts the value x into the nums array at index 0
- time complexity -> O(n)
- extra space complexity if relevant -> None
- one-sentence reason -> The time complexity is O(n) because it shifts every element in the array over by one spot to the right.
5. nums.insert(len(nums), x)
- what it does / returns -> this essentially just does the same as append where you add an element to the end of a list
- time complexity -> I mean O(1) if the length of the array isnt at capacity
- extra space complexity if relevant -> if the length is at capacity then you will need to allocate more space 
- one-sentence reason -> This example appends a value to the end of an array just like append()
6. nums.pop()
- what it does / returns -> returns the value of the last element in the list and removes it from the list
- time complexity -> O(1)
- extra space complexity if relevant -> none
- one-sentence reason -> time complexity is O(1) because nothing shifts and we have direct access to the location 
7. nums.pop(2)
- what it does / returns -> this removes an element from a list at index 2
- time complexity -> O(n) 
- extra space complexity if relevant -> none
- one-sentence reason -> time complexity is O(n) because all of the elements that follow have to shift to the left over one spot 
8. nums.remove(x)
- what it does / returns -> This will look for value x in the list and remove it whereever the first iteration is in the array. returns error if value is not in array
- time complexity -> O(n)
- extra space complexity if relevant -> None
- one-sentence reason -> The time complexity is O(n) because in worst case remove has to search the whole array for the value where it could be at the end or not exist at all. 
Also, if the value is found anywhere in the array then you still have to search up until that point and then remove that value which requires shifting all of the elements on the left.
9. x in nums
- what it does / returns -> returns a boolean on whether or not the value is in the array
- time complexity -> O(n)
- extra space complexity if relevant -> None
- one-sentence reason -> this has to search through the array item by item to find the value if it exists so O(n) time complexity
10. nums.index(x)
- what it does / returns -> returns an integer that represents the location of the first iteration of value x.
- time complexity -> O(n)
- extra space complexity if relevant -> None
- one-sentence reason -> same as 'x in nums' reasoning
11. nums[:]
- what it does / returns -> it creates a shallow copy of nums
- time complexity -> O(n)
- extra space complexity if relevant -> O(n)
- one-sentence reason -> it creates a new array of same size of nums (which is why O(n) space comp) and it populates the array with n references.
12. nums[a:b]
- what it does / returns -> returns shallow copy of nums[a:b] where a is starting index included and b is end index excluded
- time complexity -> m is size of shallow copy so O(m)
- extra space complexity if relevant -> O(m)
- one-sentence reason -> same as the resoning for nums[:] just a different window into the nums list
13. nums.reverse()
- what it does / returns -> it reverses an iterable in place and returns nothing I think or None
- time complexity -> O(n)
- extra space complexity if relevant -> O(1)
- one-sentence reason -> reversing means you have to move each element which scales with n so O(n) time complexity 
14. nums[::-1]
- what it does / returns -> its the same as the .reverse() but it creates a shallow copy and returns that copy
- time complexity -> O(n)
- extra space complexity if relevant -> O(n)
- one-sentence reason Creates a new array storing the same references as nums but in a different order.
15. nums.sort()
- what it does / returns -> sorts nums in ascending order in-place
- time complexity -> O(nlogn)
- extra space complexity if relevant -> pyhton uses tim something which includes extra space but we can just say O(1)
- one-sentence reason -> essentially n times you have to sort something so n * logn 
16. sorted(nums)
- what it does / returns -> creates an array of all of nums references but in sorted order
- time complexity -> O(nlogn)
- extra space complexity if relevant -> O(n)
- one-sentence reason -> same reasoning as above but I think that this maybe returns a shallow copy so O(n) space
17. nums.extend(other) where len(other) = k
- what it does / returns -> python copies the references from other and appends them to available slots in nums
- time complexity -> O(m) where m is the length of other. Could be O(n + m) if by appending these items nums.size outgrows capacity.
- extra space complexity if relevant -> if nums outgrows capacity then yes
- one-sentence reason
18. That is potentially O(n^2) because for each reference in nums we are performing an operation whos time complexity is O(n)
"""
