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

################################### NOTE #################################################
 THERE ARE MANY WAYS THIS PROBLEM CAN BE SOLVED , IN THIS SOLUTION WE WILL BE USING OOP
##########################################################################################

================================== Coding With Clifford ===================================
"""
class Calc_FVal():
    def __init__(self): # automatically executes when an instance of the class is created
        self.get_values() # automatically calls when an instance of the class is created
        self.calc_future_val() #automatically calls when an instance of the class is created

    #this method is used to get the values from the user(keyboard)
    def get_values(self):
        self.P_val=float(input("Enter the present value of the account  :")) # reads the present value
        self.i_val=float(input("Enter the monthly interest rate (in %)  :")) # reads the interest rate
        self.t_val=int(input(  "Enter the number months                 :")) # reads the number of months

    # this method calculates and display the future value
    def calc_future_val(self):
        #F = Px(1 + i) ^ t
        self.f_value=self.P_val*(1+(self.i_val)/100)**self.t_val #calculates the future value
        print("*****"*10)
        #it displays the future value
        print("When the present value is R{0} at {1}% rate , the future value should "
              "be R{3} after {2} months".format(self.P_val,self.i_val,self.t_val,self.f_value))
        print("*****" * 10)


number=Calc_FVal() # creates an instance of the Calc_FVal() class






#                                                            CODING WITH CLIFFORD
