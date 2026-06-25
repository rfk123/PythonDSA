# Create a list an loop through it
nums = [1, 2, 3, 4, 5, 6]
print("Looping through the nums in nums")
for num in nums:
    print(num)

print('----------------------------------')

print("Looping through the index in nums")
for i in range(len(nums)):
    print(i)

print('----------------------------------')

print("Looping through the nums and index in nums")
for i, num in enumerate(nums):
    print(i, num)

print('----------------------------------')

age = 30
print("Conditional printing with logical statements")
if age > 80:
    print(str(age) + "-" + "Old")
elif age < 80 and age > 35:
    print(str(age) + "-" + "Middle-aged")
else:
    print(str(age) + "-" + "Young")

print('----------------------------------')
