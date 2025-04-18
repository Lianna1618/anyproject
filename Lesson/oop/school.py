# Parrent class: Lesson lists
class Global_lists:
    def __init__(self):
        self.lesson_prices = {
            "HR": 50000,
            "PM": 45000,
            "QA": 480000,
            ".Net": 28000,
            "Node.js": 70000,
            "SMM": 20000,
            "Marketing": 30000,
            "Design": 32000,
        }

    def check_brand(self, brand):
        # Check if the lesson exists in the market
        return brand in self.lesson_prices


# Child class: Lesson
class Lesson(Global_lists):
    def __init__(self):
        super().__init__()
        self.discount = 0.20  # 20% discount for Node.js

    def print_result(self, brand):
        if self.check_brand(brand):
            if brand == "Node.js":
                # Apply 20% discount for Node.js
                discounted_price = self.lesson_prices[brand] * (1 - self.discount)
                print(f"Price of {brand} with 20% discount: ${discounted_price:.2f}")
            else:
                # Print the price for other brands
                print(f"Price of {brand}: ${self.lesson_prices[brand]}")
        else:
            # Brand does not exist in the market
            print(f"{brand} does not exist in the list.")


# Test cases
all_lists = Global_lists()
one_lesson = Lesson()

# Check if a brand exists
print(all_lists.check_brand("Node.js"))  # Output: True
print(all_lists.check_brand("Sales"))  # Output: False

# Print results based on the brand
one_lesson.print_result("Node.js")
one_lesson.print_result("QA")
one_lesson.print_result("Sales")


# Output:
# Price of Node.js with 20% discount: $56000.00
# Price of QA: $480000
# Sales does not exist in the list.
