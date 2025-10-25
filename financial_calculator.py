import math

# Ask the user what calculation they would like to perform
calculate = input(
    "Choose either 'Bond' or 'Investment' from the menu below to proceed:\n\
Bond\t        -   To calculate the amount you'll have to pay on a bond.\n\
Ivestment\t   -   To calculate the amount of interest you'll earn.\n\
Enter your choice here: "
).lower()


# If user chooses investment ask them to enter input
if calculate == "investment":
    price = int(input("How much will you be depositing?: R "))

    rate = int(input("How much interest would you like?: "))

    time = int(input("How many years will you be investing for?: "))

    #   Ask the user what type of interest they would like
    interest = input(
        "Would you like to calculate your 'Simple' or 'Compound' intrest?: "
    ).lower()

    #   If simple is selected perform simple interest calculation
    if interest == "simple":
        amount = price * (1 + ((rate / 100) * time))

        #   Display the amount given the user input
        print(f"Your investment on maturity is: {math.ceil(amount)}")

    #   If coumpound is selected perform compound interest calculation
    elif interest == "compound":
        amount = price * (math.pow(1 + (rate / 100), time))

        #   Display the amount given the user input
        print(f"Your investment on maturity is: {math.ceil(amount)}")

# If Bond is selected ask user to enter inputs
else:
    price = float(input("Enter the present value of your house.:R "))

    interest = float(input("Enter the interest rate.: "))

    months = float(input("Number of months of repayment: "))

    # Calculate the total amount paid
    rate = (((interest / 100) / 12) * price) / (
        1 - (1 + ((interest / 100) / 12)) ** (-months)
    )

    # Display the amount
    print(f"The amount that you will pay monthly is: R {math.ceil(rate)}")
