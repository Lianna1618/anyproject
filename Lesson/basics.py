# 1. Calculate the length of a string

my_string = 'Here is string for your exercise!'
length = len(my_string)
print("Length of the string:", length)

# 2. Get a string made of the first 2 and last 2 chars


def first_last_two_chars(s):
    if len(s) < 2:
        return s * 2
    return s[:2] + s[-2:]


# Test cases
print(first_last_two_chars("w3resource"))  # Output: 'w3ce'
print(first_last_two_chars("w3"))  # Output: 'w3w3'
print(first_last_two_chars("w"))  # Output: 'ww'

# 3. Add 'ing' at the end of a string


def add_ing(s):
    return s + "ing"


# Test case
print(add_ing("abc"))  # Output: 'abcing'

# 4. Replace the last character in a string with another character


def replace_last_char(s, c):
    return s[:-1] + c


# Test case
print(
    replace_last_char("last", "p")
)  # Output: 'last' -> 'lasp'


# 5. Reverse 123 to 321 in text

def reverse_123(s):
    return s.replace("123", "321")

# Test case
print(reverse_123("abc123xyz"))  # Output: 'abc321xyz'
print(reverse_123("123abc"))  # Output: '321abc'
print(reverse_123("abc"))  # Output: 'abc'


# 6. Replace all occurrences of 'five' with 'one' in a string


def replace_five_with_one(s):
    return s.replace("five", "one")


# Test case
print(replace_five_with_one("five five was a race horse, two two was one too."))
# Output: "one one was a race horse, two two was one too."


# 7. Print the perimeter of a triangle

def triangle_perimeter(a, b, c):
    return a + b + c

# Test case
print("Perimeter of the triangle:", triangle_perimeter(3, 4, 8))  # Output: 15


# 8. Check if a value is in a group of values


def is_value_in_group(value, group):
    return value in group


# Test cases
print(is_value_in_group(3, [1, 5, 8, 3]))  # Output: True   
print(is_value_in_group(6, [1, 5, 8, 3]))  # Output: False  

# 9. Solve (x + y) * (x + y)


def solve_equation(x, y):
    return (x + y) ** 2


# Test case
x, y = 4, 3
print(f"({x} + {y}) ^ 2 =", solve_equation(x, y))  # Output: 49


# 10. Convert float to integer, sum, and reverse the result

def convert_sum_reverse(a, b):
    int_a = int(a)
    int_b = int(b)
    total = int_a + int_b
    reversed_total = int(str(total)[::-1])
    return reversed_total

# Test case
print(convert_sum_reverse(12.34, 56.78))  # Output: 86 -> 68
