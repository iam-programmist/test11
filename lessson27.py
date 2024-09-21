# def difference(numbers):
#     if len(numbers) == 0:
#         return 0
#     min_num = numbers[0]
#     max_num = numbers[0]
#     for i in numbers:
#         if i < min_num:
#             min_num = i
#         if i > max_num:
#             max_num = i
#     return max_num - min_num
# lst = difference(list(map(int,input().split())))
# print(lst)

# import random
# tickets_set = set()
# while len(tickets_set) < 100:
#     ticket = ''.join(random.choices('0123456789', k=10))
#     tickets_set.add(ticket)
# tickets = list(tickets_set)
# winners = random.sample(tickets, 2)
# for winner in winners:
#     print(winner)

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#     @abstractmethod
#     def get_area(self):
#         pass
#     @abstractmethod
#     def get_perimeter(self):
#         pass
# class Rectangle(Shape):
#     def get_area(self):
#         return self.width * self.length
#     def get_perimeter(self):
#         return 2 * (self.width + self.length)
# class Square(Shape):
#     def __init__(self, side):
#         super().__init__(side, side)
#     def get_area(self):
#         return self.width * self.length
#     def get_perimeter(self):
#         return 4 * self.width
# rect = Rectangle(5, 10)
# print(rect.get_area())
# print(rect.get_perimeter())
# square = Square(7)
# print(square.get_area())
# print(square.get_perimeter())
  
# class Staff:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
#     def display_info(self):
#         print(f"Role: {self.role}")
#         print(f"Department: {self.department}")
#         print(f"Salary: {self.salary}")
# class Leader(Staff):
#     def __init__(self, role, department, salary, team_size):
#         super().__init__(role, department, salary)
#         self.team_size = team_size
#     def display_info(self):
#         super().display_info()
#         print(f"Team Size: {self.team_size}")
# leader = Leader("Team Leader", "IT", 5000, 10)
# leader.display_info()

# with open("my_file.txt","a+") as file:
#     file.write("Hello World \n TEST \n Tajikistan \n An apple")
#     print(file)

# def test(a):
#     lst=input().split()
#     for i in len(lst):
#         if i.split>=5:
#             i=="#"
#         print(i)
# a=input()
# test(a)
