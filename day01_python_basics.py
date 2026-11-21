"""Day 1: Python basics practice.

Problems:
1. Reverse a string
2. Find the largest number in a list (without max())
3. Check whether a string is a palindrome
4. Count vowels in a string
5. Sum of even numbers in a list
"""


# 1. Reverse a string
def rev_string(s):
    result = ""
    for ch in s:
        result = ch + result  # put each new character at the front
    return result


# 2. Largest number in a list (without max())
def largest_num(nums):
    if not nums:  # empty list has no largest number
        return None
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest


# 3. Palindrome check (ignores capital letters)
def is_palindrome(s):
    s = s.lower()
    rev = ""
    for ch in s:
        rev = ch + rev
    return s == rev


# 4. Count vowels
def vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count


# 5. Sum of even numbers
def sum_even(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total


# ---------- Tests ----------
print("1. Reverse string")
print(rev_string("hello"))        # olleh
print(rev_string(""))             # (empty line)

print("2. Largest number")
print(largest_num([4, 9, 2, 7]))  # 9
print(largest_num([-5, -2, -8]))  # -2
print(largest_num([5]))           # 5
print(largest_num([]))            # None

print("3. Palindrome")
print(is_palindrome("madam"))     # True
print(is_palindrome("Madam"))     # True
print(is_palindrome("hello"))     # False
print(is_palindrome(""))          # True

print("4. Vowels")
print(vowels("i am teacher"))     # 5
print(vowels("AEIOU"))            # 5
print(vowels("rhythm"))           # 0

print("5. Sum of evens")
print(sum_even([1, 2, 3, 4, 5, 6]))  # 12
print(sum_even([1, 3, 5]))           # 0
print(sum_even([]))                  # 0
print(sum_even([-2, 4]))             # 2