
#Example - 3 -- Inheritance  

import os 
os.system('cls')
print()


class Person3:
 def __init__(self, fname1, lname2, age3 ):
    self.fname = fname1
    self.lname = lname2
    self.age   = age3

class Student(Person3):    ### inheritance 
  def __init__(self, fname, lname, age, year):
    super().__init__(fname, lname, age)
    self.graduationyear = year
  
  def print_record(self):    ## method  
    print( "\n 303 Name  : " , self.fname, self.lname ,  "  Age : " ,  self.age, "  Passing Year : ",  self.graduationyear , "\n ") 

 
# Main Part
x = Student("Mike", "Olsen", 30, 2019)
 
x.print_record() 

x.fname="mamun" ;   x.graduationyear=2020 ;  x.age=50  
print( "\n 304 Name  : " , x.fname, x.lname ,  "  Age : " ,  x.age, "  Passing Year : ",  x.graduationyear , "\n ") 

print()

# 303 Name  :  Mike Olsen    Age :  30   Passing Year :  2019 
# 304 Name  :  mamun Olsen   Age :  50   Passing Year :  2019



