# Script to standardise payments of recurring rental payments
# This script takes the total rental amount, the number of months, and the frequency of payments as input
# And calculate the standardised monthly amount.

def calculate_standard_payment(total_amount, num_months, frequency):
    if frequency not in ("monthly", "quarterly", "annually"):
        raise ValueError("Invalid frequency. Choose 'monthly', 'quarterly', or 'annually'.")

    if frequency == "monthly":
        return total_amount / num_months
    elif frequency == "quarterly":
        return total_amount / (num_months / 3)
    elif frequency == "annually":
        return total_amount / (num_months / 12)

def main():
    try:
        # prompt you for the necessary information.
        total_amount = float(input("Enter the total rental amount: "))
        num_months = int(input("Enter the number of months: "))
        frequency = input("Enter the frequency of payments (monthly/quarterly/annually): ").lower()

        # calculate the standardized payment amount based on the given frequency.
        standard_payment = calculate_standard_payment(total_amount, num_months, frequency)
        print(f"The standardized {frequency} payment amount is: {standard_payment:.2f}")
    except ValueError as e:
        print("Error", e)

if __name__ == "__main__":
    main()

