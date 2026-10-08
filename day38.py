"""
1. nums[i]
- what it does / returns -> returns the value in nums at index i
- time complexity -> O(1)
- extra space complexity if relevant -> No
- one-sentence reason -> Quick lookup of what value is being held at index i in array nums
2. nums[i] = x
- what it does / returns -> This updates the value in nums at the ith index to equal x (or to have the reference of x)
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
- one-sentence reason -> If I remember correctly, if this method fails it returns an error? 
5. nums.insert(len(nums), x)
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
6. nums.pop()
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
7. nums.pop(2)
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
8. nums.remove(x)
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
9. x in nums
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
10. nums.index(x)
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
11. nums[:]
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
12. nums[a:b]
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
13. nums.reverse()
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
14. nums[::-1]
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
15. nums.sort()
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
16. sorted(nums)
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason
17. nums.extend(other) where len(other) = k
- what it does / returns
- time complexity
- extra space complexity if relevant
- one-sentence reason

"""
