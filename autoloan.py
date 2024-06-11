Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
menWomen = input("Are you a man or woman? (This will affect the insurance rate):\n")
age = int(input("What is your age?: \n"))
credit_score = int(input("What is your credit score?: \n"))
newUsedVehicle = input("Is the vehicle you are purchasing new or used?: \n")
loan = int(input("What is the loan amount?: \n"))
down_payment = int(input("what is your down payment?: \n"))
loan_term = int(input("How long did you get your loan for?(Enter in months):\n"))

maleInsuranceRate = [640, 568, 505, 383, 345, 285, 261, 244, 228,
                     202, 178, 174, 172, 170, 165, 160, 159, 163, 173]

womenInsuranceRate = [586, 515, 547, 346, 312, 263, 245, 230,
                      218, 197, 179, 176, 174, 172, 165, 159, 158, 161, 170]

# average rate based off of credit score and new or used vehicle. by credit score
avg_interestRate_New = [15.62, 12.85, 9.62, 6.89, 5.38]  # 15.62
avg_interestRate_Used = [21.57, 18.97, 13.72, 9.04, 6.80]

# This will pick the insurance rate
if menWomen == "man":
    if age == 16:
        menInsureRate = maleInsuranceRate[0]
    elif age == 17:
        menInsureRate = maleInsuranceRate[1]
    elif age == 18:
        menInsureRate = maleInsuranceRate[2]
    elif age == 19:
        menInsureRate = maleInsuranceRate[3]
    elif age == 20:
        menInsureRate = maleInsuranceRate[4]
    elif age == 21:
        menInsureRate = maleInsuranceRate[5]
    elif age == 22:
        menInsureRate = maleInsuranceRate[6]
    elif age == 23:
        menInsureRate = maleInsuranceRate[7]
    elif age == 24:
        menInsureRate = maleInsuranceRate[8]
    elif 25 <= age <= 29:
        menInsureRate = maleInsuranceRate[9]
    elif 30 <= age <= 34:
        menInsureRate = maleInsuranceRate[10]
    elif 35 <= age <= 39:
        menInsureRate = maleInsuranceRate[11]
    elif 40 <= age <= 44:
        menInsureRate = maleInsuranceRate[12]
    elif 45 <= age <= 49:
        menInsureRate = maleInsuranceRate[13]
    elif 50 <= age <= 54:
        menInsureRate = maleInsuranceRate[14]
    elif 55 <= age <= 59:
        menInsureRate = maleInsuranceRate[15]
    elif 60 <= age <= 64:
        menInsureRate = maleInsuranceRate[16]
    elif 65 <= age <= 69:
        menInsureRate = maleInsuranceRate[17]
    else:
        menInsureRate = maleInsuranceRate[18]
    print(f"your interest rate will be ${menInsureRate}")
if menWomen == "woman":
    if age == 16:
        womanInsureRate = womenInsuranceRate[0]
    elif age == 17:
        womanInsureRate = womenInsuranceRate[1]
    elif age == 18:
        womanInsureRate = womenInsuranceRate[2]
    elif age == 19:
        womanInsureRate = womenInsuranceRate[3]
    elif age == 20:
        womanInsureRate = womenInsuranceRate[4]
    elif age == 21:
        womanInsureRate = womenInsuranceRate[5]
    elif age == 22:
        womanInsureRate = womenInsuranceRate[6]
    elif age == 23:
        womanInsureRate = womenInsuranceRate[7]
    elif age == 24:
        womanInsureRate = womenInsuranceRate[8]
    elif 25 <= age <= 29:
        womanInsureRate = womenInsuranceRate[9]
    elif 30 <= age <= 34:
        womanInsureRate = womenInsuranceRate[10]
    elif 35 <= age <= 39:
        womanInsureRate = womenInsuranceRate[11]
    elif 40 <= age <= 44:
        womanInsureRate = womenInsuranceRate[12]
    elif 45 <= age <= 49:
        womanInsureRate = womenInsuranceRate[13]
    elif 50 <= age <= 54:
        womanInsureRate = womenInsuranceRate[14]
    elif 55 <= age <= 59:
        womanInsureRate = womenInsuranceRate[15]
    elif 60 <= age <= 64:
        womanInsureRate = womenInsuranceRate[16]
    elif 65 <= age <= 69:
        womanInsureRate = womenInsuranceRate[17]
    else:
        womanInsureRate = womenInsuranceRate[18]
    print(f"your interest rate will be ${womanInsureRate}")
# for new and used vehicles. Based on the credit score you will receive interest
if newUsedVehicle == "new":
    if 300 <= credit_score <= 500:
        rate = avg_interestRate_New[0]
    elif 501 <= credit_score <= 600:
        rate = avg_interestRate_New[1]
    elif 601 <= credit_score <= 660:
        rate = avg_interestRate_New[2]
    elif 661 <= credit_score <= 780:
        rate = avg_interestRate_New[3]
    elif 781 <= credit_score <= 850:
        rate = avg_interestRate_New[4]

if newUsedVehicle == "used":
    if 300 <= credit_score <= 500:
        rate = avg_interestRate_Used[0]
    elif 501 <= credit_score <= 600:
        rate = avg_interestRate_Used[1]
    elif 601 <= credit_score <= 660:
        rate = avg_interestRate_Used[2]
    elif 661 <= credit_score <= 780:
        rate = avg_interestRate_Used[3]
    elif 781 <= credit_score <= 850:
        rate = avg_interestRate_Used[4]

actual_loan = loan - down_payment

broke_down_rate = (rate / 12) / 100.


i = rate * .0100  # the interest 2 decimal places to the left
monthly_payment = (actual_loan) * (i / 12) / (1 - (1 + (i / 12)) ** (-loan_term))

loanLoop = actual_loan
total = 0

while loanLoop >= 0:
    interest = broke_down_rate * loanLoop
    amortized = monthly_payment - broke_down_rate * loanLoop
    balance = loanLoop - amortized

    loanLoop -= amortized
    total += interest


print(f"The total insurance you will pay is: ${'{:,.2f}'.format(total)}")
print(f"Altogether with the loan and interest you will be paying: ${'{:,.2f}'.format(actual_loan + total)}")
print(f"your monthly payment will be: ${'{:,.2f}'.format(monthly_payment)}")
