def twoSum(nums, target):
    num_to_index = {}  # Map from number to its index

    for i, num in enumerate(nums):
        diff = target - num

        if diff in num_to_index:
            return [num_to_index[diff], i]

        num_to_index[num] = i

    return []

print(twoSum([2,9,11,15],13))