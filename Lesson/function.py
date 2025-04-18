1.0


def text(x):
    print("any text", x, "yfhg")


text(10)
# Output: any text 10 yfhg


# 2. happy_birthday function


def full_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


print(full_name("Lianna", "Tavadyan"))


def happy_birthday(name, age, wish):
    print(f"Happy birth dear {name} !!!")
    print(f"You are {age} old!!")
    print(f"{wish}")


happy_birthday("name", 20, "Good luck")


# 3 Determine the season based on month and day of the month


def determine_season(month, day):
    if (month == 12 and day >= 21) or (month <= 3 and day < 20):
        return "Winter"
    elif (month == 3 and day >= 20) or (month <= 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (month <= 9 and day < 22):
        return "Summer"
    else:
        return "Autumn"


# Input
month = 7  # July
day = 31

# Output
print(f"Month: July({month})")
print(f"Day: {day}")
print(f"Season: {determine_season(month, day)}")


# 4. Count the number of letters and digits in a string


def count_letters_digits(s):
    letters = 0
    digits = 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return letters, digits


data = "BTC appeared in 2009"
letters, digits = count_letters_digits(data)
print(f"Letters: {letters}")
print(f"Digits: {digits}")


# 5. Find the median of a list of numbers


def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


# Test lists
numbers1 = [15, 26, 28, 33]
numbers2 = [1, 4, 5, 6, 7]
numbers3 = [1, 3, 3, 6, 7, 8, 9]
numbers4 = [1, 2, 3, 4, 5, 6, 8, 9]

# Output
print("Median of numbers1:", find_median(numbers1))  # Output: 27.0
print("Median of numbers2:", find_median(numbers2))  # Output: 5
print("Median of numbers3:", find_median(numbers3))  # Output: 6
print("Median of numbers4:", find_median(numbers4))  # Output: 4.5
