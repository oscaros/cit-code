# class change:
#     def __init__(self, x, y, z):
#         self.a = x + y + z #6
 
# x = change(1,2,3)
# y = getattr(x, 'a') 
# setattr(x, 'a', y+1)
# print(x.a)

# class fruits:
#     def __init__(self, price):
#         self.price = price
# obj=fruits(50)
 
# obj.quantity=10
# obj.bags=2
 
# print(obj.quantity+len(obj.__dict__))


# class Demo:
#     def __init__(self):
#         pass
 
#     def test(self):
#         print(__name__)
 
# obj = Demo()
# obj.test()

# class A:
#     def __init__(self):
#         self.multiply(15)
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 4 * i;
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def multiply(self, i):
#         self.i = 2 * i;
# obj = B()

class Demo:
    def check(self):
        return " Demo's check "
    def display(self):
        print(self.check())
class Demo_Derived(Demo):
    def check(self):
        return " Derived's check "
Demo().display()
Demo_Derived().display()




class Std_Name:   
    def __init__(self, Std_firstName, Std_Phn, Std_lastName):  
        self.Std_firstName = Std_firstName  
        self.Std_PhnStd_Phn = Std_Phn  
        self.Std_lastName = Std_lastName  
   
Std_firstName = "Wick"  
name = Std_Name(Std_firstName, 'F', "Bob")  
Std_firstName = "Ann"  
name.lastName = "Nick"  
print(name.Std_firstName, name.Std_lastName) 
