import math  


def main():
#TO DO  
    Leg_A = float(input("Enter length of Leg A: "))         #Asking for inputs to two legs
    Leg_B = float(input("Enter length of Leg B: "))
    pythag(Leg_A,Leg_B)                                     #Calling pythag with the two legs as arguments     

def pythag(A,B):
#TO DO  
    Hypotenuse = math.sqrt(A**2 + B**2)                     #Calculate the hypotenuse with imported math and using pythagorean theorem 
    print(f"The length of the hypotenuse is: {Hypotenuse}") 
    print(f"The hypotenuse rounded to 2dp would be {round(Hypotenuse,2)}")  #Have a cleaned up version of the hypotenuse output to 2dp



main()
