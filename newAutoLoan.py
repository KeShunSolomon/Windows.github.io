import math


def newPersonalLoan():
    global womanInsureRate, womenInsureRate, menInsureRate, menWomen, loan, monthly_payment_women, monthly_payment_men
    again = 'yes'  # loops the program
    while again == "yes":
        age = int(input("What is your age?: \n"))
        credit_score = int(input("What is your credit score?: \n"))
        loan = int(input("What is the loan amount?: \n"))
        loan_month = int(input("How long did you get your loan for?(Enter in months):\n"))
        newUsedVehicle = input("Is the vehicle you are purchasing new or used?: \n")  # Determines the interest rate
        down_payment = int(input("what is your down payment?: \n"))
        menWomen = input("Are you a man or woman? (This will affect the insurance rate):\n")
        vehicle_price = int(input("How much does the vehicle cost?: \n"))

        # list of insurance per month by age and gender
        femaleInsuranceRate = [586, 515, 457, 346, 312, 263, 245, 230, 218,
                               197, 179, 176, 174, 172, 165, 159, 158, 161, 170]

        maleInsuranceRate = [640, 568, 505, 383, 345, 285, 261, 244, 228,
                             202, 178, 174, 172, 170, 165, 160, 159, 163, 173]

        # average rate based off of credit score and new or used vehicle
        avg_interestRate_New = [14.78, 12.28, 9.60, 7.01, 5.64]
        avg_interestRate_Used = [21.55, 18.89, 14.12, 9.73, 7.66]

        while menWomen == "woman":
            if age == 16:
                womenInsureRate = femaleInsuranceRate[0]
            elif age == 17:
                womenInsureRate = femaleInsuranceRate[1]
            elif age == 18:
                womenInsureRate = femaleInsuranceRate[2]
            elif age == 19:
                womenInsureRate = femaleInsuranceRate[3]
            elif age == 20:
                womenInsureRate = femaleInsuranceRate[4]
            elif age == 21:
                womenInsureRate = femaleInsuranceRate[5]
            elif age == 22:
                womenInsureRate = femaleInsuranceRate[6]
            elif age == 23:
                womenInsureRate = femaleInsuranceRate[7]
            elif age == 24:
                womenInsureRate = femaleInsuranceRate[8]
            elif 25 <= age <= 29:
                womenInsureRate = femaleInsuranceRate[9]
            elif 30 <= age <= 34:
                womenInsureRate = femaleInsuranceRate[10]
            elif 35 <= age <= 39:
                womenInsureRate = femaleInsuranceRate[11]
            elif 40 <= age <= 44:
                womenInsureRate = femaleInsuranceRate[12]
            elif 45 <= age <= 49:
                womenInsureRate = femaleInsuranceRate[13]
            elif 50 <= age <= 54:
                womenInsureRate = femaleInsuranceRate[14]
            elif 55 <= age <= 59:
                womenInsureRate = femaleInsuranceRate[15]
            elif 60 <= age <= 64:
                womenInsureRate = femaleInsuranceRate[16]
            elif 65 <= age <= 69:
                womenInsureRate = femaleInsuranceRate[17]
            else:
                womenInsureRate = femaleInsuranceRate[18]

        while menWomen == "man":
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


        # newVehiclePrice = vehicle_price - down_payment

        # this is the loan amount because the down payment and vehicle price
        # probably take out loan and just have the user ask about the loan month
        # also change the loan below to true loan amount
        # look at toyota website after it is done for correct solutions
        # true_loan_amount = vehicle_price - down_payment

        # calculating monthly payments for women
        divide_womenRate = (womenInsureRate / 12)
        part_payment = (loan) * (divide_womenRate)
        # this is going to be divided by part_payment
        lowerDivide_womenRate = (1-(1+womenInsureRate/12))
        most_payment = (part_payment) / (lowerDivide_womenRate)
        monthly_payment_women = most_payment ** -loan_month

        # calculating monthly payments for men
        divide_menRate = (menInsureRate / 12)
        part_payment = (loan) * (divide_menRate)
        # this is going to be divided by part_payment
        lowerDivide_menRate = (1 - (1 + menInsureRate / 12))
        most_payment = (part_payment) / (lowerDivide_menRate)
        monthly_payment_men = most_payment ** -loan_month


        # calculating the amortized interest
        #for females
    if menWomen == 'woman' or menWomen == 'Woman':
        interest_monthly_payment = (womenInsureRate / 12) / 100

        month_of_interest = interest_monthly_payment * loan

        amortized_interest = month_of_interest - monthly_payment_women

    if menWomen == 'man' or menWomen == 'Man':
        # calculating the amortized interest
        # for males
        interest_monthly_payment = (menInsureRate / 12) / 100

        month_of_interest = interest_monthly_payment * loan

        amortized_interest = month_of_interest - monthly_payment_men
newPersonalLoan()
