"""
Problem:  Implement the inheritance function

Sample Input : User define  

Platform: Self study

Difficulty: Easy 

"""

class Employee:
     def __init__(self , name , id):
          self.name = name
          self.id = id


     def empDetails(self):
          print(f"The Employee Details : {self.id} {self.name}")


emp = Employee("Vaibhav Pawar" , 45)
emp.empDetails()
emp1 = Employee("Rohit Sharma" , 99)
emp1.empDetails()