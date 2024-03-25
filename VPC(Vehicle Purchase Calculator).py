Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import math
'''This program calculates the loan amount for a new or used car. 
   The program tells you how much you have to pay for loan, insurance, and how much does the money you pay goes back
   to the interest.'''
def vehicleLoan():


    again = 'y' # loops the program, so it will run as many times as you like to
    while again == "y":

        user_age = int(input("what is your age? \n")) # age of the user
        user_CS = int(input("What is your Credit Score? \n"))# credit score of the user
        loan = int(input("How much is your loan?\n")) # The loan the user is getting for the vehicle

        # The loan_year is the amount of time you want it to be to pay off the loan. This will turn into months when configuring
        loan_year = int(input("What year loan are you getting? (Note:The shorter then loan the less you will pay in the long run.\nRecommend picking a loan no more than 48 months.) \n"))

        vehicle_NewUsed = input("Is the vehicle new or used? \n") # This will determine the interest rate depending on the vehicle


        # List of insurance by age and the average credit rate with new and used vehicle
        insurance_list = [584.42, 501.33, 436.75, 344.67, 307.75, 248.08, 166.17, 145.42, 142.58, 139.67, 137.33, 126.17, 130.33, 157.17, 198.92] # list of insurance per month by age
        avg_NewCredit = [12.83, 10.11, 7.25, 4.90, 3.84]
        avg_UsedCredit = [19.81, 15.86, 9.81, 5.47, 3.69]

        # If the user enter the age the insure_price will become the correct number for the insurance
        #** neg. num might be faster than going through the whole list** ask a professor and see
        if user_age == 16:
            insure_price = insurance_list[0]
        elif user_age == 17:
            insure_price = insurance_list[1]
        elif user_age == 18:
            insure_price = insurance_list[2]
        elif user_age == 19:
            insure_price = insurance_list[3]
        elif user_age == 20:
            insure_price = insurance_list[4]
        elif user_age == 21 or user_age <= 24:
            insure_price = insurance_list[5]
        elif user_age == 25 or user_age <= 29:
            insure_price = insurance_list[6]
        elif user_age == 30 | user_age <= 34:
            insure_price = insurance_list[7]
        elif user_age == 35 or user_age <= 39:
            insure_price = insurance_list[8]
        elif user_age == 40 or user_age <= 44:
            insure_price = insurance_list[-6]
        elif user_age == 45 or user_age <= 54:
            insure_price = insurance_list[-5]
        elif user_age == 55 or user_age <= 64:
            insure_price = insurance_list[-4]
        elif user_age == 65 or user_age <= 74:
            insure_price = insurance_list[-3]
        elif user_age == 75 or user_age <= 84:
            insure_price = insurance_list[-2]
        else:
            insure_price = insurance_list[-1]



        # This function is for new and used vehicles. Based on the credit score you will receive interest
        if vehicle_NewUsed == "new":
            if user_CS == 300 or user_CS < 501:
                rate = avg_NewCredit[0]
            elif user_CS == 501 or user_CS < 601:
                rate = avg_NewCredit[1]
            elif user_CS == 601 or user_CS < 661:
                rate = avg_NewCredit[2]
            elif user_CS == 661 or user_CS < 781:
                rate = avg_NewCredit[3]
            else:
                rate = 6.0

        if vehicle_NewUsed == "used":
            if user_CS == 300 or user_CS < 501:
                rate = avg_UsedCredit[0]
            elif user_CS == 501 or user_CS < 601:
                rate = avg_UsedCredit[1]
            elif user_CS == 601 or user_CS < 661:
                rate = avg_UsedCredit[2]
            elif user_CS == 661 or user_CS < 781:
                rate = avg_UsedCredit[3]
            else:
                rate = avg_UsedCredit[4]

# calculating monthly payment. May be fixed

        monthly_interest = (rate / 12) / 100

        repayment_term = loan_year * 12
        num_1 = monthly_interest + 1
        num_2 = (round(num_1 ** repayment_term,4))
        formula = round((round(monthly_interest * num_2,4)) / (round(num_2 - 1,4)),4)
        monthly_payment = loan * formula

# print(f"monthly payment: {monthly_payment}")






# calculating amortized interest. this will calculate how much interest accumulated over time.

        i = (math.ceil(loan * 100) / 100)
        total = 0
        m_payment = monthly_payment

        while i > 0:

            monthly_interest = (rate / 12) / 100
            interest = round(monthly_interest * i,2)
            principal = m_payment - interest
            balance = loan - principal

            i -= principal
            total += interest



        print("Age:", user_age,"\nCredit Score:", user_CS, "\nYour loan amount is:", loan )
        print(f"Your loan year is:{loan_year:,d}")
        print(f"With all of the information you have given me the insurance will cost ${insure_price}.\nThe rate on your {vehicle_NewUsed} vehicle will be {rate}% and your monthly payment will be ${round(monthly_payment,2)} per month. In the course of this time you would pay ${round(total,2)} amount in interest.")
        print(f"The total you will pay per month is roughly ${round(insure_price + monthly_payment,2)}.\n")
        again = input("Would you like to calculate again? type y/n:\n")

        if again == 'n':
            break
        outfile = open('userinfo.txt', 'a')

if __name__ == '__main__':
    vehicleLoan()