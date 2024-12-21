income = float(input("Enter your income: "))
if income > 50000:
    credit_score = int(input("Enter your credit score: "))
    if credit_score > 700:
        print("Loan approved\n")
    elif 600 <= credit_score <= 700:
        print("Loan approved with a higher interest rate\n")
    else:
        print("Loan rejected\n")
else:
    print("Loan rejected\n")