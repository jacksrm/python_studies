# nums = (2, 5, 9, 1)
# nums[2] = 3 -> Error! Tuples are immutable
# print(nums)

nums = [2, 5, 9, 1]
nums[2] = 3  # OK
# nums[4] = 7 # Error! Cant add elements this way
nums.append(7)
print(nums)
