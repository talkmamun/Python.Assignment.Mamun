import os 
os.system('cls')
print()


class person:
 def __init__(self, name, age):
    self.name=name
    self.age=age

p1 = person("john", 48)
p1.age=47
print ("\n Name  :  " , p1.name , "      Age : ", p1.age)
#   Name  :   john       Age :  47

# Example - 2 
class person:
 def __init__(self, name, age):
    self.name=name
    self.age=age
 
 def __str__(self):
    return f"{self.name}({self.age})"
    #return str(self.name) + "(" + str(self.age) +")\n"

p1 = person("rahim", 32)
print(p1)

s = p1.name  ,   p1.age 
print (s)
#rahim(32)



print ( "\nExample - 3") 
class person:
 def __init__(self, name, age):
    self.name=name
    self.age=age
 
 def print_name(s):
    return f"{s.name}  age ({s.age})"
    #return str(self.name) + "(" + str(self.age) +")\n"

p1 = person("rahim", 32)
print("304 p1.print_name()   :   ", p1.print_name())


print ()



