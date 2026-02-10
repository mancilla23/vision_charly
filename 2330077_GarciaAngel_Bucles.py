# Problem 1: Sum of integers in a range
# Description:
#   This program calculates the sum of all integers from 1 to n
#   (inclusive). It also calculates the sum of only the even numbers
#   in the same range using a for loop.
#
# Inputs:
#   - n (int): upper limit of the range
#
# Outputs:
#   - "Sum 1..n:" <total_sum>
#   - "Even sum 1..n:" <even_sum>
#
# Validations:
#   - n must be convertible to int
#   - n >= 1
#   If validation fails, show "Error: invalid input"
#
# Test cases:
#   1) Normal: n = 10
#   2) Edge case: n = 1
#   3) Error: n = -5 or n = "abc"

try:
    n = int(input("Enter a positive integer (n >= 1): "))

    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except ValueError:
    print("Error: invalid input")


# Problem 2: Multiplication table with for
# Description:
#   This program generates and displays the multiplication table
#   of a base number from 1 up to a limit m.
#
# Inputs:
#   - base (int)
#   - m (int): table limit
#
# Outputs:
#   - One line per multiplication:
#     "base x i = result"
#
# Validations:
#   - base and m must be convertible to int
#   - m >= 1
#   If validation fails, show "Error: invalid input"
#
# Test cases:
#   1) Normal: base = 5, m = 4
#   2) Edge case: base = 3, m = 1
#   3) Error: base = 7, m = 0

try:
    base = int(input("Enter the base number: "))
    m = int(input("Enter the limit (m >= 1): "))

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            result = base * i
            print(f"{base} x {i} = {result}")

except ValueError:


# Problem 3: Average of numbers with while and sentinel
# Description:
#   This program reads numbers one by one until a sentinel value is entered.
#   It calculates the average of valid numbers and the count of values read.
#   If no valid data is entered, it shows an error message.
#
# Inputs:
#   - number (float, read repeatedly)
#   - sentinel_value (fixed in code)
#
# Outputs:
#   - "Count:" <count>
#   - "Average:" <average_value>
#   - If no valid data: "Error: no data"
#
# Validations:
#   - Each input must be convertible to float
#   - Only numbers >= 0 are accepted
#   - Sentinel value is ignored in calculations
#
# Test cases:
#   1) Normal: 10, 20, 30, -1
#   2) Edge case: 5, -1
#   3) Error: -1 (no valid data), "abc"
# --------------------------------------------------

SENTINEL_VALUE = -1

total_sum = 0.0
count = 0

while True:
    user_input = input("Enter a number (or -1 to finish): ")

    try:
        number = float(user_input)
    except ValueError:
        print("Error: invalid input")
        continue

    if number == SENTINEL_VALUE:
        break

    if number < 0:
        print("Error: invalid input")
        continue

    total_sum += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print("Count:", count)
    print("Average:", average)


# Problem 4: Password attempts with while
# Description:
#   This program implements a simple password attempt system.
#   The user has a limited number of attempts to enter the correct password.
#
# Inputs:
#   - user_password (string; read on each attempt)
#
# Outputs:
#   - "Login success" if the password is correct within the limit
#   - "Account locked" if all attempts are used
#
# Validations:
#   - MAX_ATTEMPTS > 0 (defined as a constant)
#   - Attempts are counted correctly
#
# Test cases:
#   1) Normal: correct password entered within attempts
#   2) Edge case: correct password on last attempt
#   3) Error: all attempts used with incorrect passwords
# --------------------------------------------------

CORRECT_PASSWORD = "sexilla"
MAX_ATTEMPTS = 3

attempts = 0
login_success = False

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")
    attempts += 1

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        login_success = True
        break

if not login_success:
    print("Account locked")


# Problem 5: Simple menu with while
# Description:
#   This program implements a text-based menu that repeats until
#   the user chooses to exit. Each option performs a specific action.
#
# Inputs:
#   - option (string or int; user choice)
#
# Outputs:
#   - "Hello!"
#   - "Counter:" <counter_value>
#   - "Counter incremented"
#   - "Bye!"
#   - "Error: invalid option"
#
# Validations:
#   - option must be convertible to int
#   - only options 0, 1, 2, 3 are valid
#
# Test cases:
#   1) Normal: 1, 3, 2, 0
#   2) Edge case: 2 (counter starts at 0)
#   3) Error: 5 or "abc"
# --------------------------------------------------

counter = 0
option = -1

while option != 0:
    print("\nMenu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    user_input = input("Choose an option: ")

    try:
        option = int(user_input)
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")


# Problem 6: Pattern printing with nested loops
# Description:
#   This program prints a right triangle pattern using nested for loops.
#   It also prints an inverted triangle pattern (optional extension).
#
# Inputs:
#   - n (int; number of rows)
#
# Outputs:
#   - Triangle pattern line by line
#   - Inverted triangle pattern
#
# Validations:
#   - n must be convertible to int
#   - n >= 1
# --------------------------------------------------

user_input = input("Enter number of rows: ")

try:
    n = int(user_input)
    if n < 1:
        print("Error: invalid input")
    else:
        # Normal triangle pattern
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)

        # Optional inverted triangle pattern
        for i in range(n, 0, -1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)

except ValueError:
    print("Error: invalid input")
