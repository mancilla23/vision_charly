# Problem 1: Full name formatter (name + initials)
# Description:
# This program receives a full name as a single string, normalizes it,
# formats it in Title Case, and generates the initials of each word.
#
# Inputs:
# - full_name (string; full name with possible extra spaces and mixed case)
#
# Outputs:
# - "Formatted name:" <Name In Title Case>
# - "Initials:" <X.X.X.>
#
# Validation:
# - full_name must not be empty after strip()
# - full_name must contain at least two words
# - If validation fails, print "Error: invalid input"
#
# Test cases:
# 1) Normal: "juan carlos tovar" → Juan Carlos Tovar, J.C.T.
# 2) Edge case: "  MARIA   lopez  " → Maria Lopez, M.L.
# 3) Error: "   " → Error

full_name = input().strip()

# Validation: not empty
if full_name == "":
    print("Error: invalid input")
else:
    # Split and remove extra spaces
    parts = full_name.split()

    # Validation: at least two words
    if len(parts) < 2:
        print("Error: invalid input")
    else:
        # Format name in Title Case
        formatted_name = " ".join(parts).title()

        # Generate initials
        initials = ""
        for word in parts:
            initials += word[0].upper() + "."

        print("Formatted name:", formatted_name)
        print("Initials:", initials)


# Problem 2: Simple email validator (structure + domain)
# Description:
# This program validates whether an email address has a basic valid structure.
# It checks for exactly one '@', at least one '.' after it, and no spaces.
# If valid, it also displays the domain part of the email.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email:" True|False
# - If valid: "Domain:" <domain_part>
#
# Validation:
# - email_text must not be empty after strip()
# - Must contain exactly one '@'
# - Must not contain spaces
# - Must contain at least one '.' after '@'
#
# Test cases:
# 1) Normal: "user@example.com" → Valid True, Domain example.com
# 2) Edge case: "test@mail.co" → Valid True, Domain mail.co
# 3) Error: "user@@mail.com" or "user mail.com" → Valid False

email_text = input().strip()

valid_email = True

# Validation: not empty
if email_text == "":
    valid_email = False

# Validation: no spaces
elif " " in email_text:
    valid_email = False

# Validation: exactly one '@'
elif email_text.count("@") != 1:
    valid_email = False

else:
    at_index = email_text.find("@")
    domain_part = email_text[at_index + 1:]

    # Validation: domain must contain at least one '.'
    if "." not in domain_part:
        valid_email = False

print("Valid email:", valid_email)

if valid_email:
    print("Domain:", domain_part)


# Problem 3: Palindrome checker (ignoring spaces and case)
# Description:
# This program checks whether a given phrase is a palindrome.
# It ignores spaces and letter case when comparing the text.
# A palindrome reads the same forward and backward.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - (Optional) Shows the normalized version of the phrase
#
# Validation:
# - phrase must not be empty after strip()
# - After removing spaces, length must be at least 3 characters
#
# Test cases:
# 1) Normal: "Anita lava la tina" → true
# 2) Edge case: "oso" → true
# 3) Error: "  " → invalid input

phrase = input().strip()

# Initial validation
if phrase == "":
    print("Is palindrome: false")
else:
    # Normalize: lowercase and remove spaces
    normalized = phrase.lower().replace(" ", "")

    # Length validation
    if len(normalized) < 3:
        print("Is palindrome: false")
    else:
        # Check palindrome
        is_palindrome = (normalized == normalized[::-1])

        print("Is palindrome:", str(is_palindrome).lower())
        print("Normalized phrase:", normalized)


# Problem 4: Sentence word statistics (lengths and first/last word)
# Description:
# This program analyzes a sentence and extracts basic word statistics.
# It counts the total number of words and identifies the first, last,
# shortest, and longest word based on length.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validation:
# - sentence must not be empty after strip()
# - There must be at least one valid word after split()
#
# Test cases:
# 1) Normal: "Python is very powerful" → 4 words
# 2) Edge case: "Hello" → first = last = shortest = longest = "Hello"
# 3) Error: "   " → invalid input

sentence = input().strip()

# Validation
if sentence == "":
    print("Error: invalid input")
else:
    words = sentence.split()

    if len(words) == 0:
        print("Error: invalid input")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]

        # Initialize shortest and longest
        shortest_word = words[0]
        longest_word = words[0]

        for word in words:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word

        print("Word count:", word_count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)


# Problem 5: Password strength classifier
# Description:
# This program classifies a password as weak, medium, or strong.
# The classification is based on length and the presence of
# uppercase letters, lowercase letters, digits, and symbols.
#
# Rules used:
# - Weak: length < 8
# - Medium: length >= 8 but does NOT meet all strong requirements
# - Strong: length >= 8 and contains at least:
#   one uppercase letter, one lowercase letter,
#   one digit, and one non-alphanumeric symbol
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validation:
# - Password must not be empty
#
# Test cases:
# 1) Normal: "Abc123!!" → strong
# 2) Edge case: "abcdefgH" → medium
# 3) Error: "" → invalid input

password_input = input()

# Validation
if password_input == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    length_ok = len(password_input) >= 8

    if not length_ok:
        strength = "weak"
    elif length_ok and has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print("Password strength:", strength)


# Problem 6: Product label formatter (fixed-width text)
# Description:
# This program generates a product label in a single line using
# a fixed width of exactly 30 characters. If the label is shorter,
# it is padded with spaces; if longer, it is truncated.
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - "Label: <exactly 30 characters>"
#
# Validation:
# - product_name must not be empty after strip()
# - price_value must be convertible to a positive number
#
# Test cases:
# 1) Normal: product_name="Apple", price=10 → padded label
# 2) Edge case: very long product name → truncated label
# 3) Error: empty product_name or negative price

product_name = input().strip()
price_value = input().strip()

# Validation
try:
    price_number = float(price_value)
    if product_name == "" or price_number <= 0:
        print("Error: invalid input")
    else:
        base_label = f"Product: {product_name} | Price: ${price_value}"

        if len(base_label) < 30:
            label = base_label + " " * (30 - len(base_label))
        else:
            label = base_label[:30]

        print(f'Label: "{label}"')

except ValueError:
    print("Error: invalid input")
