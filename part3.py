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
     return credits
     """
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

def histo(x,y):
     """
     Last modified: 4/29/2021
     Author: Geeth Muthunayaka
     Input parameters: number(int) and type of outcome(str) 
     Function: Histogram
     """
     print(f"{y:9} {x} : {'*'*x}")
     

progress=0
trailer=0
retriever=0
exclude=0
print('-'*40)
print("Staff Version with Histogram \n")
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
        if fail_credit>=80:
            print("Exclude")
            exclude+=1
        elif pass_credit==120 :
            print("Progress")
            progress+=1
        elif pass_credit==100:
            print("Progress(module trailer)")
            trailer+=1
        else:
            print("Do not Progress – module retriever")
            retriever+=1
            
        outcome=exclude+progress+trailer+retriever
        question=input("\nWould you like to enter another set of data?\nEnter 'q' to quit and view results or any other key to continue: ")
        print()
        question=question.lower()
        
        if question=="q":
            print("-"*40)
            print("Horizontal Histogram")
            
            histo(progress,"Progress")
            histo(trailer,"Trailer")
            histo(retriever,"Retriever")
            histo(exclude,"Exclude")
            
            print(f"\n{outcome} outcomes in total.")
            print("-"*40)
            break
            
        
    except ValueError:
        print("Integer required\n")

