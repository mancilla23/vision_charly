# Problem 1: Shopping list basics
# Description:
# This program works with a shopping list using basic list operations.
# It creates an initial list of products, allows adding a new product,
# checks if a product exists, and shows the total number of items.

# Inputs:
# - initial_items_text (string): products with quantities (e.g. "apple:2,banana:5")
# - new_item (string): product to add.
# - search_item (string): product to search.

# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <number_of_items>
# - "Found item:" True | False

# Validations:
# - initial_items_text must not be empty.
# - new_item and search_item must not be empty.
# - All product names are stored and searched in lowercase.

# Test cases:
# 1) Normal: "apple:2,banana:5", new_item="orange", search_item="apple" → Found True
# 2) Edge case: one initial item only → List size = 2 after adding
# 3) Error: empty initial_items_text → Error: invalid input


initial_items_text = input("Enter initial items: ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    items_list = []

    raw_items = initial_items_text.split(",")

    for item in raw_items:
        product = item.split(":")[0].strip().lower()
        if product != "":
            items_list.append(product)

    new_item = input("Enter new item: ").strip().lower()
    search_item = input("Enter item to search: ").strip().lower()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        items_list.append(new_item)

        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", search_item in items_list)


# Problem 2: Points and distances with tuples
# Description:
# This program uses tuples to represent two points in a 2D plane.
# It calculates the Euclidean distance between them and the midpoint.

# Inputs:
# - x1, y1, x2, y2 (float): coordinates of the points.

# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)

# Validations:
# - All inputs must be convertible to float.

# Test cases:
# 1) Normal: (0,0) and (4,0) → Distance = 4.0, Midpoint = (2.0, 0.0)
# 2) Edge case: same points → Distance = 0.0
# 3) Error: non-numeric input → Error: invalid input


try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: invalid input")



# Problem 3: Product catalog with dictionary
# Description:
# This program manages a simple product catalog using a dictionary.
# It allows the user to select a product and a quantity, then calculates
# the total price if the product exists in the catalog.

# Inputs:
# - product_name (string): name of the product to buy.
# - quantity (int): quantity to purchase.

# Outputs:
# - "Unit price:" <unit_price>
# - "Quantity:" <quantity>
# - "Total:" <total_price>
# - Or "Error: product not found"

# Validations:
# - product_name must not be empty.
# - quantity must be greater than 0.
# - product_name must exist in the dictionary.

# Test cases:
# 1) Normal: product_name="apple", quantity=3 → Total = 30.0
# 2) Edge case: product_name="banana", quantity=1 → Total = 8.5
# 3) Error: product_name="milk", quantity=2 → Error: product not found


product_prices = {
    "apple": 10.0,
    "banana": 8.5,
    "orange": 12.0
}

product_name = input("Enter product name: ").strip().lower()

if product_name == "":
    print("Error: product not found")
else:
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Error: invalid input")
        else:
            if product_name in product_prices:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity

                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
            else:
                print("Error: product not found")

    except ValueError:
        print("Error: invalid input")


# Problem 4: Student grades with dict and list
# Description:
# This program manages student grades using a dictionary where each
# student has a list of numeric grades. It calculates the average
# and determines whether the student has passed.

# Inputs:
# - student_name (string): name of the student to search.

# Outputs:
# - If the student exists:
#   - "Grades:" <grades_list>
#   - "Average:" <average_value>
#   - "Passed:" True | False
# - If the student does not exist:
#   - "Error: student not found"

# Validations:
# - student_name must not be empty after strip().
# - student_name must exist as a key in the dictionary.
# - The grades list must not be empty.
# - Grades are assumed to be in the range 0–100.

# Test cases:
# 1) Normal: student_name="alice" → Average calculated, Passed True/False
# 2) Edge case: student with empty grades list → Error
# 3) Error: student_name not in dictionary → Error: student not found


grades = {
    "alice": [90, 85, 88],
    "bob": [70, 65, 72],
    "carol": [95, 92, 90]
}

student_name = input("Enter student name: ").strip().lower()

if student_name == "":
    print("Error: student not found")
elif student_name not in grades:
    print("Error: student not found")
else:
    grades_list = grades[student_name]

    if len(grades_list) == 0:
        print("Error: student not found")
    else:
        average = sum(grades_list) / len(grades_list)
        is_passed = average >= 70.0

        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", is_passed)


# Problem 5: Word frequency counter (list + dict)
# Description:
# This program counts the frequency of each word in a sentence.
# It converts the sentence to lowercase, removes basic punctuation,
# stores the words in a list, and builds a dictionary with frequencies.

# Inputs:
# - sentence (string): a sentence entered by the user.

# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <frequency_dictionary>
# - "Most common word:" <word>

# Validations:
# - sentence must not be empty after strip().
# - The words list must not be empty.
# - Basic punctuation is removed using replace().

# Test cases:
# 1) Normal: "Hello world hello" → hello appears twice
# 2) Edge case: "Python!" → one word, frequency 1
# 3) Error: "" → Error: invalid input


sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    # Remove basic punctuation
    punctuation = [".", ",", "!", "?", ";", ":"]
    for symbol in punctuation:
        sentence = sentence.replace(symbol, "")

    sentence = sentence.lower()
    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        frequency_dict = {}

        for word in words_list:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1

        most_common_word = ""
        max_frequency = 0

        for word, count in frequency_dict.items():
            if count > max_frequency:
                max_frequency = count
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", frequency_dict)
        print("Most common word:", most_common_word)


# Problem 6: Simple address book (dictionary CRUD)
# Description:
# This program implements a simple address book using a dictionary.
# It allows the user to add, search, or delete contacts by name,
# following basic CRUD operations.

# Inputs:
# - action_text (string): "ADD", "SEARCH", or "DELETE".
# - name (string): contact name (depends on action).
# - phone (string): phone number (only for ADD).

# Outputs:
# - For ADD:
#   - "Contact saved:" <name> <phone>
# - For SEARCH:
#   - "Phone:" <phone>
#   - Or "Error: contact not found"
# - For DELETE:
#   - "Contact deleted:" <name>
#   - Or "Error: contact not found"

# Validations:
# - action_text must be one of: ADD, SEARCH, DELETE.
# - name must not be empty after strip().
# - phone must not be empty for ADD.
# - Names are normalized using strip().title().

# Test cases:
# 1) Normal: ADD "Alice" "123456" → Contact saved
# 2) Edge case: SEARCH existing contact → Phone displayed
# 3) Error: DELETE non-existing contact → Error message


contacts = {
    "Alice": "1111111111",
    "Bob": "2222222222",
    "Carol": "3333333333"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")
else:
    name = input("Enter contact name: ").strip().title()

    if name == "":
        print("Error: invalid input")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()

            if phone == "":
                print("Error: invalid input")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")
