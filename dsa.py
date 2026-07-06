# import re


# arrray = [7,3,9,2,8,10]

# def second(arr):
#     first  = 0
#     second  = 0
#     for i in range(len(arr)):
#         if arr[i] > first:
#             second = first
#             first  = arr[i]
#         elif second<first and second != first:
#             second = arr[i]
#     return first,second

# # print(second(arrray))

# k = [5,7,8,3,7,8,9,2,3]


# def security(j):
#     k = {}
#     for i in j:
#         if i not in k:
#             k[i] =0
#         else:
#             k[i] +=1
#     answer = len([x for x in k.values() if x >= 1])
#     return k,answer

# # print(security(k))


# # l = [1,2,3,4,5,6,7,8,9]
# # l[::2] = 10,20,30,40,50
# # print(l)



# # a = [1,2,3,4,5,6,7,8,9]
# # print(a[3:0:-1])

# # arr  = [[1,2,3,4],
# #         [4,5,6,7],
# #         [8,9,10,11],
# #         [12,13,14,15,16],

# # ]
# # for i in range(0,4):
# #     print(arr[i].pop(),end=" ")


# # def f(i,va= []):
# #     va.append(i)
# #     return va

# # f(1)
# # f(2)
# # f(3)
# # print(f(4))

# # k = 9
# # for i in range(1,k):
# #     print(i,k-i)



# # def distance(li):
# #     gap = []
# #     for i in range(1,len(li)):
# #         gap.append(abs(li[i]-abs(li[i-1])))
# #         print(gap)
# #     return sum(gap)

# # print(distance([10,11,7,12,14]))



# # class new:
# #     def __init__(self):
# #         self.a=10


# # obj1 = new()
# # obj2 = new()
# # obj3 = new()    
# # obj1.a = 20
# # print(obj1.a,obj2.a,obj3.a)


# # #single level inheritance
# # class college:
# #     def college_name(self):
# #        print("college name is ABC")

# # class student(college):
# #     def student_name(self):
# #         print("student name is XYZ")
# #         self.college_name()

# # obj = student()
# # obj.college_name()
# # obj.student_name()



# # #sachin chnages 


# # def addthiscode():
# #         name = "aryan"
# #         name3 = "sachin"
# #         print(name,name3)
        
# # addthiscode()



# # ##multiple level inheritance
# # class college:
# #     def college_name(self):
# #        print("college name is ABC")
# # class student(college):
# #     def student_name(self):
# #         print("student name is XYZ")
# #         self.college_name()
# # class marks(student):
# #     def marks(self):
# #         print("marks is 90")
# #         self.student_name()


# # obj = marks()
# # obj.college_name() 


# # class arthematic:
# #     def add(self):
# #         a = int(input("ENTER THE NUBER"))
# #         b = int(input("ENTER THE NUBER"))
# #         return a+b
# # A  = arthematic()
# # print(A.add())



# # class arthematic:
# #     def add(self, a):
# #         print (a)
    
# #     def add(self, a , b):
# #         print(a+b)

# #     def add(self, a, b, c):
# #         print(a+b+c)

# # obj = arthematic()
# # obj.add(10,20,30)
# # obj.add(10,20)
# # obj.add(10)




# # class arthematic:
# #     def __init__(self, a=None, b=None, c=None):
        
# #         if(a is None and b is None and c is None):
# #             print("all are none")
# #         elif( b is None and c is None):
# #             print()
# #         elif(c is None):
# #             print(a)

# # obj = arthematic()
# # obj = arthematic(10)
# # obj = arthematic(10, 20)
# # obj = arthematic(10, 20, 30)





# # class Rbi:
# #     def carloan(self):
# #         print("car loan is 10%")
# #     def homeloan(self):
# #         print("home loan is 8%")
    
# # class Sbi(Rbi):
    
# #     def homeloan(self):
# #         print("home loan is 7%")
# #         super().homeloan()


# # sbi = Sbi()
# # sbi.homeloan()




# # class Father:
# #     def __init__(self):
# #         print("father class")

# # class child(Father):
# #     def __init__(self):
# #         print("child class")
# #         super().__init__()
# # obj = child()



# class base:
#     def __init__(self):
#         self.a = "prashant"
#         #single underscore =  " protectedd"
#         #dounble underscoer  = private

#         self._c = "ashsihg"
#         self.k  = self.__c
#         self.k = "aruan"
#         print(self.k)

# class derived(base):
#     def __init__(self):
#         base.__init__(self)
#         print("calling private member of base class")
#         print(self.a)
#         print(self._C)


# # obj1 = derived()
# # print(obj1.a)
# # print(obj1.__c)
# # obj2 = base()
# # print(obj2.a)

# class rbi:
#     def publicpolicy(self):
#         print("check the publiv policy of RBI")
#     def __private(self):
#         print("there is some private policy 0")
    
# class sbi(rbi):
#     def __int__(self):
#         rbi.__init__(self)
#     def callingpublic(self):
#         print("\n inside")
#         self.publicpolicy()
#     def callingprivatemethod(self):
#         self.__private()

# obj1 = sbi()
# obj1.callingpublic()
# obj1.callingprivatemethod()

# obj1.publicpolicy()

# obj1.__private()
# obj2  = rbi()
# obj2.publicpolicy()
# obj2.__private()
# obj2.publicpolicy()
# obj2.__rbi__private()

import re

with open("array.txt", "w") as f:
    f.write("This is a sample text file.\n")
    f.write("It contains some text data.\n")
    f.write("We will use regular expressions to search for patterns.\n")
    f.write("Regular expressions are powerful for text processing.\n")
    f.write("Let's find all the words that start with 's'.\n")

k = open("array.txt", "r")
data = k.read()
k.close()
a  = input("enter the term to search: "
           )

match = re.search(a,data)

if match:
    print("match found")
    print("matched text:", match.group())
    print("start index:", match.start())
    print("end index:", match.end())

else:
    print("match not found")