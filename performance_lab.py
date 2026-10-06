# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
        counts = {}

        for number in numbers:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1

        most_common = None
        highest_count = 0

        for number, count in counts.items():
            if count > highest_count:
                highest_count = count
                most_common = number
        return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) because we still go through the list to count occurrences.
- Worst-case: O(n) because for each number is checked and stored in the dictionary.
- Average-case: O(n) because the dictionary lookups are normally O(1).
- Space complexity: O(n) because the dictionary may store every number.
- Why this approach? A dictionary makes it easy to keep track of how many times the numbers appear.
- Could it be optimized? I think its pretty efficient, maybe python counter could be used to make it more concise but the time complexity would be the same.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    # Your code here
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case:O(n) becasue we still have to go through the list to check for duplicates.
- Worst-case: O(n) because we have to check each number and store it in the set.
- Average-case: O(n) becasue we still have to see if a set is nrmally O(1). 
- Space complexity: O(n) because the set may store every number.
- Why this approach? A set makes it fast to check and see if a number was already seen and the list keeps the numbers in their orginal order. 
- Could it be optimized? This is pretty efficent I think the only other thing we could try to not use a set but then that woould  only make there be less space but the code would be slower. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]


#original version
def find_pairs_original(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs
#optimized version
def find_pairs(nums, target):
    # Your code here
    seen = set()
    pairs = set()
    
    for num in nums:
        needed = target - num
        if needed in seen:
            pairs.add((needed, num))
        seen.add(num)
    return (pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) becasue we still go through the whole list.
- Worst-case: O(n) because we have to check each number and store it in the set.
- Average-case: O(n) becasue we still have to see if a set is normally O(1).
- Space complexity: O(n) becasue the set and pairs list can grow with the input.
- Why this approach? This approach is used becasue it is fast to check if the number needs to make the target sum and the set keeps track of what we have seen.
- Could it be optimized? I think that a nested loop could maybe be helpful for less space but again it would be slower. 
"""
"""
Optimiziation
- The orginal solution used nested loops which had O(n^2) time complexity.
- I decided to optimze it by using a set to keep track of the numbers.
- The version is optimized to O(n) time complexity because we only loop through the list once and use a set for O(1) lookups.
- The trad off however is that the optimized version uses O9N) extra space.
- I choose problem three to optimize because i want it to preform better with larger lists. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    # Your code here
    capacity = 1
    items = []
    for i in range(n):
        if len(items) == capacity:
            old_capacity = capacity
            capacity *= 2
            print(f"Resizing from {old_capacity} to {capacity}")

            new_list = [0]
            for item in items:
                new_list.append(item)
            items = new_list
        items.append(i)
    return items

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list reaches its capacity.
- What is the worst-case for a single append? O(n) becasue all the existing items may need to be copied into a bigger set. 
- What is the amortized time per append overall? O(1) because the cost of resizing is spread out over many appends.
- Space complexity: O(n) because the list can grow to hold all nunbers.
- Why does doubling reduce the cost overall? Doubling gives the list more room so it does not have to resize every time. 
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    # Your code here
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) because we still have to go through the list to compute the running total.
- Worst-case: O9n) because every number has to be added and processed.
- Average-case: O(n) becasue the loop alwasy runs once for every number. 
- Space complexity: O(n) because we make a new list the same size as the ouput.
- Why this approach? This approach is used becasue it is simple and efficient to keep a running total and append it to the new list.
- Could it be optimized? I think this is very efficeint and can not think of a change. 
"""

#tests
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # Output: 3
print(most_frequent([5, 5, 2, 2, 5]))  # Output: 5
print(most_frequent([7]))  # Output: 7
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # Output: [4, 5, 6, 7]
print(remove_duplicates([1, 1, 1, 1]))  # Output: [1]
print(remove_duplicates([]))  # Output: []
print(find_pairs([1, 2, 3, 4], 5)) # Output: [(2, 3), (1, 4)]
print(find_pairs([2, 4, 6, 8], 10)) # Output: [(4, 6), (2, 8)]
print(find_pairs([1, 2, 3], 10)) # Output: []
print(add_n_items(6))  # Should print resizing messages
print(add_n_items(10))  # Should print resizing messages
print(add_n_items(0))  # Should not print anything
print(running_total([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]
print(running_total([5, 10, 15]))  # Output: [5, 15, 30]
print(running_total([]))  # Output: []