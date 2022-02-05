# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830175         
  
# Date: 4/29/2021

print('-'*40)

pass_credit=int(input("Please enter your credits at pass : "))
defer_credit=int(input("Please enter your credits at defer : "))
fail_credit=int(input("Please enter your credits at fail : "))

if fail_credit>=80:
    print("Exclude")

elif pass_credit==120:
    print("Progress")

elif pass_credit==100:
    print("Progress (module trailer)")

else:
    print("Do not Progress – module retriever")
    
print('-'*40)
