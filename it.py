def get_user_input():
    while True:
        try:
            income = float(input("Enter your annual income: "))
            if income < 0:
                raise ValueError("Income should be a non-negative number.")
            return income
        except ValueError as e:
            print(f"Error: {e}")

def get_deductions():
    while True:
        try:
            deductions = float(input("Enter your total deductions: "))
            if deductions < 0:
                raise ValueError("Deductions should be a non-negative number.")
            return deductions
        except ValueError as e:
            print(f"Error: {e}")

def calculate_taxable_income(income, deductions):
    return max(income - deductions, 0)

def calculate_income_tax(taxable_income, brackets, rates):
    remaining_income = taxable_income
    tax_paid = 0

    for i in range(len(brackets)):
        if remaining_income > 0:
            bracket_size = min(remaining_income, brackets[i])
            tax_paid += bracket_size * rates[i]
            remaining_income -= bracket_size

    return tax_paid

def display_tax_info(brackets, rates):
    print("\nTax Brackets and Rates:")
    for i in range(len(brackets) - 1):
        print(f"${brackets[i]:,} - ${brackets[i + 1]:,}: {rates[i] * 100}%")
    print(f"Over ${brackets[-1]:,}: {rates[-1] * 100}%")

def main():
    # Define tax brackets and rates
    brackets = [10000, 30000, 70000, 100000]
    rates = [0.1, 0.2, 0.3, 0.4, 0.5]

    # Get user input for income and deductions
    income = get_user_input()
    deductions = get_deductions()

    # Calculate taxable income
    taxable_income = calculate_taxable_income(income, deductions)

    # Calculate income tax
    income_tax = calculate_income_tax(taxable_income, brackets, rates)

    # Display results
    print(f"\nYour annual income: ${income:,.2f}")
    print(f"Total deductions: ${deductions:,.2f}")
    print(f"Taxable income: ${taxable_income:,.2f}")
    display_tax_info(brackets, rates)
    print(f"\nYour income tax is: ${income_tax:,.2f}")

if __name__ == "__main__":
    main()


