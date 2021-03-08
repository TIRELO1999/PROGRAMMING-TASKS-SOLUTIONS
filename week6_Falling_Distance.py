"""

----------------------------------- PROBLEM STATEMENT -----------------------------------
When an object is falling because of gravity, the following formula can be
used to determine the distance the object falls in a specific time period:
D = (1/2)(g)(t^2)
The variables in the formula are as follows:
-D is the distance in meters,
-g is the gravitational force,which is 9.8N, and
-t is the amount of time in seconds that the object has been falling.,
Write a program that accepts an object’s falling time (in seconds). The program
should return the distance, in meters, that the object has fallen during that
time (write an appropriate comment).
----------------------------------------------------------------------------------------


================================ Coding With Clifford ===================================

"""

# this method takes the time the object has been falling from the user(keyboard) and display the results
def main():
    time=float(input("Enter the time( in seconds ) the object has been falling :")) #time the object has been falling
    grav_force="9.8 N" # gravitational force
    print("*****"*29)
    print("When the object has been falling at a for {0} seconds,with gravitational force of {1} , "
          "it will fall for {2} meters".format(time,grav_force,calc_FD(time)))
    print("*****" * 29)

#this method calculates the distance the object has been falling
def calc_FD(time_val):
    Distance=(0.5)*(9.8)*(time_val**2) #calculates the falling distance
    return Distance

main()# calls the main method






#                                                            CODING WITH CLIFFORD