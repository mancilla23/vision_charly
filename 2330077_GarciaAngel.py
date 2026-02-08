# Problem 1: Rectangle area and perimeter (basic functions)
# Description:
#   This program defines two functions to calculate the area and
#   perimeter of a rectangle. The main code asks the user for input,
#   validates it, and displays the results.
#
# Inputs:
#   - width (float)
#   - height (float)
#
# Outputs:
#   - "Area:" <area_value>
#   - "Perimeter:" <perimeter_value>
#
# Validations:
#   - width > 0
#   - height > 0
#   If validation fails, show "Error: invalid input" and do not call functions.
#
# Test cases:
#   1) Normal: width=5, height=3
#   2) Edge case: width=0.1, height=0.1
#   3) Error: width=-4, height=2
# --------------------------------------------------

def calculate_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def calculate_perimeter(width, height):
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


try:
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))

    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)

        print("Area:", area)
        print("Perimeter:", perimeter)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")


# Problem 2: Grade classifier (function with return string)
# Description:
#   This program defines a function that classifies a numeric score
#   (0–100) into a letter grade. The main code asks the user for the
#   score, validates it, and displays the result.
#
# Inputs:
#   - score (float or int)
#
# Outputs:
#   - "Score:" <score>
#   - "Category:" <grade_letter>
#
# Validations:
#   - 0 <= score <= 100
#   If validation fails, show "Error: invalid input" and do not classify.
#
# Test cases:
#   1) Normal: score = 85
#   2) Edge case: score = 90
#   3) Error: score = 120
# --------------------------------------------------

def classify_grade(score):
    """Return the letter grade according to the score value."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter the score (0-100): "))

    if 0 <= score <= 100:
        category = classify_grade(score)
        print("Score:", score)
        print("Category:", category)
    else:
        print("Error: invalid input")

except ValueError:
    print("Error: invalid input")


# Problem 3: List statistics function (min, max, average)
# Description:
#   This program defines a function that receives a list of numbers
#   and returns a dictionary with the minimum, maximum, and average.
#   The main code asks the user for a comma-separated list of numbers,
#   validates the input, and displays the results.
#
# Inputs:
#   - numbers_text (string; example: "10,20,30")
#   - Internally: numbers_list (list of float)
#
# Outputs:
#   - "Min:" <min_value>
#   - "Max:" <max_value>
#   - "Average:" <average_value>
#
# Validations:
#   - numbers_text not empty after strip()
#   - list not empty after conversion
#   - all elements must be valid numbers
#
# Test cases:
#   1) Normal: "10,20,30"
#   2) Edge case: "5"
#   3) Error: "10, abc, 20"
# --------------------------------------------------

def summarize_numbers(numbers_list):
    """Return a dictionary with min, max, and average values."""
    minimum = min(numbers_list)
    maximum = max(numbers_list)
    average = sum(numbers_list) / len(numbers_list)

    return {
        "min": minimum,
        "max": maximum,
        "average": average
    }


try:
    numbers_text = input("Enter numbers separated by commas: ").strip()

    if not numbers_text:
        print("Error: invalid input")
    else:
        parts = numbers_text.split(",")
        numbers_list = []

        for part in parts:
            number = float(part.strip())
            numbers_list.append(number)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            result = summarize_numbers(numbers_list)
            print("Min:", result["min"])
            print("Max:", result["max"])
            print("Average:", result["average"])

except ValueError:
    print("Error: invalid input")



# Problem 4: Apply discount list (pure function)
# Description:
#   This program defines a pure function that receives a list of prices
#   and a discount rate, and returns a new list with discounted prices.
#   The original list is not modified.
#
# Inputs:
#   - prices_text (string; example: "100,200,300")
#   - discount_rate (float between 0 and 1)
#
# Outputs:
#   - "Original prices:" <original_list>
#   - "Discounted prices:" <discounted_list>
#
# Validations:
#   - prices_text not empty after strip()
#   - resulting list not empty
#   - all prices > 0
#   - 0 <= discount_rate <= 1
#
# Test cases:
#   1) Normal: prices_text="100,200,300", discount_rate=0.10
#   2) Edge case: prices_text="50", discount_rate=0
#   3) Error: prices_text="100,-20,50", discount_rate=1.5
# --------------------------------------------------

def apply_discount(prices_list, discount_rate):
    """Return a new list with discounted prices (pure function)."""
    discounted_prices = []

    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_prices.append(discounted_price)

    return discounted_prices


# Main code
try:
    prices_text = input("Enter prices separated by commas: ").strip()
    discount_rate = float(input("Enter discount rate (0 to 1): "))

    if not prices_text or not (0 <= discount_rate <= 1):
        print("Error: invalid input")
    else:
        parts = prices_text.split(",")
        prices_list = []

        for part in parts:
            price = float(part.strip())
            if price <= 0:
                raise ValueError
            prices_list.append(price)

        if len(prices_list) == 0:
            print("Error: invalid input")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)

            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)

except ValueError:
    print("Error: invalid input")



# Problem 5: Greeting function with default parameters
# Description:
#   This program defines a greeting function that optionally includes
#   a title before the name. The main code asks the user for input,
#   validates it, and shows the greeting message.
#
# Inputs:
#   - name (string)
#   - title (string, optional)
#
# Outputs:
#   - "Greeting:" <greeting_message>
#
# Validations:
#   - name not empty after strip()
#   - title may be empty, but if not, it is normalized using strip()
#
# Test cases:
#   1) Normal: name="Alice", title="Dr."
#   2) Edge case: name="Bob", title=""
#   3) Error: name="   "
# --------------------------------------------------

def greet(name, title=""):
    """Return a greeting message with optional title."""
    clean_name = name.strip()
    clean_title = title.strip()

    if clean_title:
        full_name = f"{clean_title} {clean_name}"
    else:
        full_name = clean_name

    return f"Hello, {full_name}!"


# Main code
try:
    name = input("Enter your name: ").strip()
    title = input("Enter your title (optional): ").strip()

    if not name:
        print("Error: invalid input")
    else:
        # Call using named arguments (as requested)
        greeting_message = greet(name=name, title=title)
        print("Greeting:", greeting_message)

except Exception:
    print("Error: invalid input")



# Problem 6: Factorial function (iterative implementation)
# Description:
#   This program defines a function to calculate the factorial of a
#   non-negative integer using an iterative approach. The iterative
#   version is used to avoid recursion depth issues and keep the
#   implementation simple and efficient.
#
# Inputs:
#   - n (int)
#
# Outputs:
#   - "n:" <n>
#   - "Factorial:" <factorial_value>
#
# Validations:
#   - n must be an integer
#   - n >= 0
#   - n <= 20 (to keep results manageable)
#
# Test cases:
#   1) Normal: n = 5
#   2) Edge case: n = 0
#   3) Error: n = -3 or n = 25
# --------------------------------------------------

def factorial(n):
    """Return n! using an iterative approach."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Main code
try:
    n = int(input("Enter a non-negative integer (0 to 20): "))

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        result = factorial(n)
        print("n:", n)
        print("Factorial:", result)

except ValueError:
    print("Error: invalid input")
