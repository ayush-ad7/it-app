def calculate_income_tax(income):
    # Define tax brackets and rates
    brackets = [10000, 30000, 70000, 100000]
    rates = [0.1, 0.2, 0.3, 0.4, 0.5]

    # Initialize variables
    remaining_income = income
    tax_paid = 0

# Calculate tax for each bracket
    for i in range(len(brackets)):
        if remaining_income > 0:
            bracket_size = min(remaining_income, brackets[i])
            tax_paid += bracket_size * rates[i]
            remaining_income -= bracket_size

    return tax_paid

# Get user input for income
try:
    income = float(input("Enter your annual income: "))
    if income < 0:
        raise ValueError("Income should be a non-negative number.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Calculate and display income tax
income_tax = calculate_income_tax(income)
print(f"Your income tax is: ${income_tax:.2f}")
