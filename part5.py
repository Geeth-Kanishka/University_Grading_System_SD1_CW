# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.

# Student ID: w1830175         
  
# Date: 4/29/2021


def histo(x,y):
     """
     Last modified: 4/29/2021
     Author: Geeth Muthunayaka
     Input parameters: number(int) and type of outcome(str) 
     Function: Histogram
     """
     print(f"{y:9} {x}: {'*'*x}")

#dataformat=[[Pass,defer,fail]...]
data=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

progress=0
exclude=0
trailer=0
retriever=0

for i in data:
    total=0
    for x in i:
        total+=x
        
    if total!=120:
        print("Total incorrect")
        
    elif i[2]>=80:
        print("Exclude")
        exclude+=1
    elif i[0]==120 :
        print("Progress")
        progress+=1
    elif i[0]==100:
        print("Progress(module trailer)")
        trailer+=1
    else:
        print("Do not Progress – module retriever")
        retriever+=1
outcome=exclude+progress+trailer+retriever
print()                
histo(progress,"Progress")
histo(trailer,"Trailer")
histo(retriever,"Retriever")
histo(exclude,"Exclude")
print(f"\n{outcome} outcomes in total.")

