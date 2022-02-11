# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830175         
  
# Date: 4/29/2021

def rangetest(credit,string):
     """
     Last modified: 4/29/2021
     Author: Geeth Muthunayaka
     Input parameters: credits(int) and credit type(str)
     Function: Checks range of the credits
     return credits """
     while credit not in range(0,121,20):
         print("Out of range.")
         credit=int(input(f"\nPlease enter your credits at {string} : "))
     return credit

def add(x=0,y=0,z=0):
     """
     Last modified: 4/29/2021
     Author: Geeth Muthunayaka
     Input parameters: 3 integers
     Function: adds upto 3 integers
     return total """
     total=x+y+z
     return total
print('-'*40)
while True:
     try:
        total=0
        while total !=120:
            pass_credit=int(input("Please enter your credits at pass : "))
            pass_credit=rangetest(pass_credit,"pass")

            defer_credit=int(input("Please enter your credits at defer : "))
            defer_credit=rangetest(defer_credit,"defer")
           
            fail_credit=int(input("Please enter your credits at fail : "))
            fail_credit=rangetest(fail_credit,"fail")

            total=add(pass_credit,defer_credit,fail_credit)
            if total!=120:
                print("Total incorrect.\n")
            
        if fail_credit >= 80:
            print("Exclude")
        elif pass_credit == 120:
            print("Progress")
        elif pass_credit == 100:
            print("Progress(module trailer)")
        else:
            print("Do not Progress – module retriever")
        break            
     except ValueError:
        print("Integer required\n")
print('-'*40)
