"""
In physics, an object that is in motion is said to have kinetic energy.
The following formula can be used to determine a moving object’s kinetic energy:
KE = (1/2)(m)(v^2)
The variables in the formula are as follows:
-KE is the kinetic energy,
-m is the object’s mass in kilograms, and
-v is the object’s velocity in meters per second.
Write a program that takes the object’s mass (in kilograms) and velocity (in meters per second)
from the user. The program should give the user the amount of kinetic energy that the object
has (write an appropriate comment).


================================ Coding With Clifford ===================================

"""

# this method takes the values of mass and velocity from the user(keyboard) and display the results
def main():
    mass=float(input("Enter the mass( in kilograms ) of the object         :"))
    vlct=float(input("Eneter the speed( in meters/seccond ) of the object  :"))
    print("*****"*23)
    print("When the object of {0} kilograms is travelling at a velocity of {1} m/s , it has the "
          "kinetic energy of {2} joules".format(mass,vlct,calc_KE(mass,vlct)))
    print("*****" * 23)

#this method calculates the value if the kinetic energy and return it
def calc_KE(mass_val,vel_val):
    KE=(0.5)*(mass_val)*(vel_val**2) #calculates the kinetic energy
    return KE

main()# calls the main method
