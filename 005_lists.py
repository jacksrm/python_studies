# nums = (2, 5, 9, 1)
# nums[2] = 3 -> Error! Tuples are immutable
# print(nums)

# nums = [2, 5, 9, 1]
# nums[2] = 3  # OK
# nums[4] = 7 # Error! Cant add elements this way
# nums.append(7)
# print(nums)

test = []
test.append("Jacson")
test.append(30)

people = []
people.append(test[:])  # change to use slicing to copy the array
print(people)

# By default you pass data by reference.
# If you want to copy an array, use the slicing technique

test[0] = "Petter"
test[1] = 40

people.append(test[:])
print(people)
