# # ---------------- BOOK ----------------
# class book():
#     def book1(self, title, author):
#         self.title = title
#         self.author = author

#     def book2(self, title1, author1):
#         self.title1 = title1
#         self.author1 = author1
#         print("book1 details:")
#         print("title:", self.title)
#         print("author:", self.author)
#         print("book2 details:")
#         print("title1:", self.title1)
#         print("author:", self.author1)


# b = book()
# b.book1("harry potter", "j.k. rowling")
# b.book2("wings of fire", "Dr. APJ Abdul Kalam")


# # ---------------- EMPLOYEE ----------------
# class employee():
#     def employee1(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def employee2(self, name1, salary1):
#         self.name1 = name1
#         self.salary1 = salary1

#         print("employee1 details:")
#         print("name:", self.name)
#         print("salary:", self.salary)
#         print("employee2 details:")
#         print("name:", self.name1)
#         print("salary:", self.salary1)


# e = employee()
# e.employee1("mohit", 100000)
# e.employee2("sumit", 90000)

# if e.salary > e.salary1:
#     print("employee 1 salary is higher.")
# else:
#     print("employee 1 salary is lower")


# # ---------------- PERSON ----------------
# class person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = person("Jay", 15)
# print("name:", p1.name)
# print("age:", p1.age)


# # ---------------- RECTANGLE ----------------
# class rectangle():
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         print("area:", self.length * self.breadth)

#     def perimeter(self):
#         print("perimeter:", 2 * (self.length + self.breadth))


# r1 = rectangle(25, 35)
# r1.area()
# r1.perimeter()


# # ---------------- VOTING ----------------
# class person2():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def check_age(self):
#         if self.age >= 18:
#             print(self.name, "you are eligible to vote")
#         else:
#             print(self.name, "you can't vote.")


# p1 = person2("jay", 18)
# p1.check_age()


# # ---------------- STUDENT ----------------
# class student():
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3

#     def result(self):
#         total = self.m1 + self.m2 + self.m3
#         average = total / 3
#         print("name:", self.name)
#         print("Total:", total)
#         print("Average:", average)


# s1 = student("himansh", 87, 67, 77)
# s1.result()


# # ---------------- MOVIE ----------------
# class movie():
#     def __init__(self, movie_name, movie_rating):
#         self.movie_name = movie_name
#         self.movie_rating = movie_rating

#     def check_movie(self):
#         if self.movie_rating >= 4:
#             print(self.movie_name, "Movie is good.")
#         else:
#             print(self.movie_name, "movie is bad.")


# m1 = movie("dhurandhar", 5)
# m1.check_movie()


# # ---------------- BONUS ----------------
# class employee_bonus():
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def check_bonus(self):
#         if self.salary > 5000:
#             bonus = self.salary * 0.10
#         else:
#             bonus = self.salary * 0.05

#         final_salary = self.salary + bonus
#         print("name:", self.name)
#         print("final_salary:", final_salary)


# e1 = employee_bonus("garv", 3000)
# e1.check_bonus()


# # ---------------- VEHICLE ----------------
# class vehicle():
#     def start(self):
#         print("vehicle started")


# class car(vehicle):
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show(self):
#         print("brand:", self.brand)
#         print("model:", self.model)


# c = car("BMW", "M5")
# c.start()
# c.show()


# # ---------------- FILE ----------------
# f = open("jay.txt", "w")
# for i in range(1, 11):
#     f.write(str(i) + "\n")
# f.close()


# # ---------------- LOOPS ----------------
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, "--even number")
#     else:
#         print(i, "--odd number")


# # ---------------- EXCEPTION ----------------
# try:
#     num1 = int(input("enter a number: "))
#     num2 = int(input("enter a second number: "))
#     result = num1 / num2
#     print(result)
# except ZeroDivisionError:
#     print("not divisible by zero.")
# except ValueError:
#     print("enter valid number")


# # ---------------- CUSTOM EXCEPTION ----------------
# class InvalidAgeError(Exception):
#     pass


# try:
#     age = int(input("enter your age: "))
#     if age < 18:
#         raise InvalidAgeError("U must be 18 or older")
#     print("granted")
# except InvalidAgeError as e:
#     print("error:", e)
# except ValueError:
#     print("enter valid age")

#-----------------------Practice-------------------------

