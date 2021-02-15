"""

Clifford works for Lesufi Tech Solutions, Inc., a software company that
has a reputation for providing excellent fringe benefits. One of their
benefits is a quarterly bonus that is paid to all employees. Another benefit
is a retirement plan for each employee. The company contributes 5% of each
employee’s gross pay and bonuses to their retirement plans. Clifford wants to
write a program that will calculate the company’s contribution to an employee’s
retirement account for a year. He wants the program to show the amount of contribution
for the employee’s gross pay and for the bonuses separately. Write a program that will
solve the problem

**********Here is a procedure to follow ***************
-Get the employee’s annual gross pay.
-Get the amount of bonuses paid to the employee.
-Calculate and display the contribution for the gross pay.
-Calculate and display the contribution for the bonuses.

==================== CODING WITH CLIFFORD ====================

"""

# the contribution rate.
CONTRIBUTION_RATE = 0.05

def main():
    #reads the gross pay and bonnus from the user
    gross_pay = float(input('Enter the gross pay: R'))
    bonus = float(input('Enter the amount of bonuses: R'))
    print("\n","*****"*3," Lesufi Tech Solutions' contribution ","*****"*3)
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

"""
The show_pay_contrib function accepts the gross
pay as an argument and displays the retirement
contribution for that amount of pay.
"""
def show_pay_contrib(gross):
    contrib_gross = gross * CONTRIBUTION_RATE # gross contribution
    print('\nContribution for gross pay: R{}'.format(contrib_gross, ',.2f'), sep='')

"""
The show_bonus_contrib function accepts the
bonus amount as an argument and displays the
retirement contribution for that amount of pay.
"""
def show_bonus_contrib(bonus):
    contrib_bonus = bonus * CONTRIBUTION_RATE # bonus contribution
    print('Contribution for bonuses: R{}'.format(contrib_bonus, ',.2f'),sep='')

# Call the main function.
main()








#                                               CODING WITH CLIFORD