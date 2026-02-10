# Problem 1: Temperature converter and range flag
# Description:
# This program converts a temperature from Celsius to Fahrenheit
# and Kelvin. It also determines whether the temperature is considered
# high based on a defined threshold.

# Inputs:
# - temp_c (float): temperature in Celsius.

# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" True | False

# Validations:
# - temp_c must be convertible to float.
# - temp_c must not be lower than -273.15 (absolute zero).

# Test cases:
# 1) Normal: temp_c = 25.0 → Fahrenheit 77.0, Kelvin 298.15, High False
# 2) Edge case: temp_c = 30.0 → High True
# 3) Error: temp_c = -300 → Error: invalid input


try:
    temp_c = float(input("Enter temperature in Celsius: "))

    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: invalid input")


# Problem 2: Work hours and overtime payment
# Description:
# This program calculates the weekly payment of a worker based on
# regular hours and overtime hours. Overtime is paid at 150% of the
# normal hourly rate and a boolean flag indicates if overtime was worked.

# Inputs:
# - hours_worked (int): number of hours worked in the week.
# - hourly_rate (float): payment per hour.

# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" True | False

# Validations:
# - hours_worked must be greater than or equal to 0.
# - hourly_rate must be greater than 0.

# Test cases:
# 1) Normal: hours_worked=45, hourly_rate=100 → overtime applied
# 2) Edge case: hours_worked=40 → no overtime
# 3) Error: hours_worked=-5 → Error: invalid input


try:
    hours_worked = int(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)

except ValueError:
    print("Error: invalid input")


# Problem 3: Discount eligibility with booleans
# Description:
# This program determines whether a customer is eligible for a discount
# based on student status, senior status, or purchase total.
# If eligible, a 10% discount is applied to the final total.

# Inputs:
# - purchase_total (float): total purchase amount.
# - is_student_text (string): "YES" or "NO".
# - is_senior_text (string): "YES" or "NO".

# Outputs:
# - "Discount eligible:" True | False
# - "Final total:" <final_total>

# Validations:
# - purchase_total must be greater than or equal to 0.0.
# - is_student_text and is_senior_text must be "YES" or "NO".
# - Inputs are normalized to uppercase before processing.

# Test cases:
# 1) Normal: purchase_total=1200, YES, NO → Discount eligible True
# 2) Edge case: purchase_total=1000, NO, NO → Discount eligible True
# 3) Error: is_student_text="MAYBE" → Error: invalid input


try:
    purchase_total = float(input("Enter purchase total: "))

    is_student_text = input("Is student? (YES/NO): ").strip().upper()
    is_senior_text = input("Is senior? (YES/NO): ").strip().upper()

    if purchase_total < 0:
        print("Error: invalid input")
    elif is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final


# Problem 4: Basic statistics of three integers
# Description:
# This program reads three integers and calculates basic statistics,
# including sum, average, maximum, minimum, and whether all values
# are even numbers.

# Inputs:
# - n1 (int): first integer.
# - n2 (int): second integer.
# - n3 (int): third integer.

# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" True | False

# Validations:
# - All inputs must be convertible to integers.
# - Negative numbers are allowed.

# Test cases:
# 1) Normal: 2, 4, 6 → All even True
# 2) Edge case: 0, -2, 4 → All even True
# 3) Error: "a", 3, 5 → Error: invalid input


try:
    n1 = int(input("Enter first integer: "))
    n2 = int(input("Enter second integer: "))
    n3 = int(input("Enter third integer: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)

except ValueError:
    print("Error: invalid input")


# Problem 5: Loan eligibility (income and debt ratio)
# Description:
# This program determines whether a person is eligible for a loan
# based on monthly income, monthly debt, and credit score.
# It calculates the debt ratio and evaluates eligibility conditions.

# Inputs:
# - monthly_income (float): monthly income amount.
# - monthly_debt (float): monthly debt payments.
# - credit_score (int): credit score value.

# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" True | False

# Validations:
# - monthly_income must be greater than 0.0.
# - monthly_debt must be greater than or equal to 0.0.
# - credit_score must be greater than or equal to 0.

# Test cases:
# 1) Normal: income=10000, debt=3000, score=700 → Eligible True
# 2) Edge case: income=8000, debt=3200, score=650 → Eligible True
# 3) Error: income=0 → Error: invalid input


try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)

except ValueError:
    print("Error: invalid input")


# Problem 6: Body Mass Index (BMI) and category flag
# Description:
# This program calculates a person's Body Mass Index (BMI)
# and determines whether the person is underweight, normal, or overweight.

# Inputs:
# - weight_kg (float): weight in kilograms.
# - height_m (float): height in meters.

# Outputs:
# - "BMI:" <bmi_rounded>
# - "Underweight:" True | False
# - "Normal:" True | False
# - "Overweight:" True | False

# Validations:
# - weight_kg must be greater than 0.0
# - height_m must be greater than 0.0

# Test cases:
# 1) weight=60, height=1.70 → Normal
# 2) weight=45, height=1.65 → Underweight
# 3) weight=90, height=1.75 → Overweight
# 4) weight=0 → Error: invalid input


try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", bmi_rounded)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)

except ValueError:
    print("Error: invalid input")
