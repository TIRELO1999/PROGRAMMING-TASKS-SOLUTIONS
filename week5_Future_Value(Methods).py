"""
********************************** PROBLEM ****************************************************

Suppose you have a certain amount of money in a savings account that earns
compound monthly interest, and you want to calculate the amount that you will
have after a specific number of months. The formula is as follows:
F =P x (1 + i)^t
The terms in the formula are:
 -F is the future value of the account after the specified time period.
 -P is the present value of the account.
 -i is the monthly interest rate.
 -t is the number of months.
Write a program that prompts the user to enter the account's present value, monthly
interest rate(in %), and the number of months that the money will be left in the account.
The program should display the account's future value after the specified number of months.

**********************************************************************************************

################################### NOTE ########################################################
 THERE ARE MANY WAYS THIS PROBLEM CAN BE SOLVED , IN THIS SOLUTION WE WILL BE USING METHODS ONLY
#################################################################################################

================================== Coding With Clifford ===================================
"""


# main method
def main():
    P_val = float(input("Enter the present value of the account  :"))  # reads the present value
    i_val = float(input("Enter the monthly interest rate (in %)  :"))  # reads the interest rate
    t_val = int(input("Enter the number months                 :"))  # reads the number of months
    calc_future_val(P_val,i_val,t_val) #calls the method calc_future_val()

# this method calculates and display the future value
def calc_future_val(P_val,i_val,t_val):
    # F = Px(1 + i) ^ t
    f_value = P_val * (1 + (i_val) / 100) ** t_val  # calculates the future value
    print("*****" * 30)
    # it displays the future value
    print("When the present value is R{0} at {1}% rate , the future value should "
            "be R{3} after {2} months".format(P_val, i_val, t_val, f_value))
    print("*****" * 30)

main()







#                                               Coding With Clifford
