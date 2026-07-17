# height = int(input("Please enter your height(cm): "))
# vip_level = int(input("Please enter your vip level: "))
# day = input(input("Please tell me what day is today?: "))

# if height < 120:
#     print("the height is below 120cm, it can be free of charge.")
# elif vip_level > 3:
#     print("vip level is higher than 3, it can be free of charge.")
# elif day == 1:
#     print("today is the first day of the month, it can be free of charge!")
# else:
#     print("sorry, your condition is not satisfied. you need to buy a ticket 10 yuan. ")

#define a variable of the number
# num = 5

# #get the guessed number of your imagination. comopare with many if and elif
# if int(input("Please guess a number: ")) == num:
#     print("Congratulations for your first correct guess!")
# elif int(input("sorry, it's wrong, Please guess another time: ")) == num:
#     print("Correct!")
# elif int(input("sorry, it's wrong, Please guess another time: ")) == num:
#     print("Correct!")
# elif int(input("sorry, it's wrong, Please guess another time: ")) == num:
#     print("Correct!")
# else:
#     print("Sorry, it's wrong!")

# print("Welcome to the Lin zoo")

# if int(input("What is your height: ")) > 120:
#     print("the height is beyond the limit, can not be free of charge!")
#     print("but, if vip is above 3, can be free of charge")

#     if int(input("What is your level: ")) > 3:
#         print("congratulations!, can be free of charge")
#     else:
#         print("Sorry, you need to buy ticket 10 yuan")
    
# else:
#     print("sorry, you can not take the present!")


# age = 20
# year = 3
# level = 1

# if age >= 18:
#     print("you are an adult")
#     if age < 30:
#         print("your age is ok")
#         if year > 2:
#             print("ok")
#         elif level > 3:
#             print("ok")
#         else:
#             print("not ok")
#     else:
#         print("not ok")
# else:
#     print("not ok")


# import random
# num = random.randint(1, 10)
# print(num)

# guess_num = int(input("Please enter your guessed number: "))

# if guess_num == num:
#     print("congratulations!")
# else:
#     if guess_num > num:
#         print("your guessed number is large")
#     else:
#         print("your guessed number is small")

#     guess_num = int(input("Please enter your guessed number again: "))

#     if guess_num == num:
#         print("congratulation, your second guess is ok")
#     else:
#         if guess_num > num:
#             print("your guessed number is large")
#         else:
#             print("your guessed number is small")
# i = 0
# while i < 100:
#     print("I love you")
#     i += 1

# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(f"1 - 100 sum is: {sum}")

# import random

# num = random.randint(1, 100)
# flag = True
# count = 0

# while flag:
#     guess_num = int(input("Please enter your guessed number: "))
#     count += 1
#     if guess_num == num:
#         print("guess!")
#         # False is the condition for terminate the loop 
#         flag = False
#     else:
#         if guess_num > num:
#             print("larger")
#         else:
#             print("small")

# print(f"you total guessed count is : {count}")

# i = 1
# while i <= 100:
#     print(f"today is the {i} day, prepare to show love...")
#     j = 1
#     while j <= 10:
#         print(f"give you the {j} roses")
#         j += 1
#     print("I love you")
#     i += 1

# print(f"stick to the {i - 1} day, succeed to show love")

# print("Hello", end = ' ')
# print("Hello", end = '')

# print("Hello\t World")
# print("itheima\t best")

# i = 1

# while i < 10:
#     j = 1
#     while j <= i:
#         print(f"{i} * {j} = {i * j}\t", end = '')
#         j += 1
#     i += 1
#     print()

# name = 'itheima'

# for x in name:
#     print(x)

# name = "itheima is a brand of itcast"
# count = 0

# for x in name:
#     if x == 'a':
#         count += 1
# print(f"the string has {count} a")

#range the first use
# for x in range(10): 
#     print(x)

# for x in range(5, 10):
#     print(x)

# for x in range(5, 10, 2):
#     print(x)

# for x in range(10):
#     print("give roses")

# a = int(input("Please enter a number: "))
# even_count = 0

# for i in range(a):
#     if (i % 2 == 0) :
#         even_count += 1
# print(even_count)
# i = 0
# for i in range(5):
#     print(i)

# print(i)

# stick to show low for 100 days
# for i in range(1, 101):
#     print(f"Today is the {i} day of showing love to the person")

#     for j in range(1, 11):
#         print(f"the {j} roses giving to the person")
    
#     print("I love the person") 

# print(f"{i} day, showing love is successful")

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i} * {j} = {i * j}\t", end = '') 
#     print()
    
# for i in range(1, 6):
#     print("the first sentence!")
#     for j in range(1, 6):
#         print("the second sentence2")
#         continue
#         print("the third sentence")
#     print("the fourth sentence")

# for i in range(1, 101):
#     print("the first sentence")
#     break
#     print("the second sentence")

# for i in range(1, 6):
#     print("the first sentence")
#     for j in range(1, 6):
#         print("the second sentence")
#         break
#         print("the third sentence")
#     print("the fourth sentence")
# money = 10000
# for i in range(1, 121):
#     import random
#     score = random.randint(1, 10)

#     if score < 5:
#         print(f"the {i} employee KPI{score}, not satisfied, ")
#         continue
    
#     if money >= 100-:
#         money -= 1000
#         print("")
# name = "itheima"
# length = len(name)
# print(length)

# str1 = "itheima"
# str2 = "itcast"
# str3 = "python"

# count = 0
# for i in str1:
#     count += 1
# print(f"the length of the string str1 is: {count}")

# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     print(f"the string {data} length is {count}")

# my_len(str1)
# my_len(str2)
# my_len(str3)

# def say():
#     print("Hello")

# say()

# def logo():
#     print("Welcome to the itheima")
#     print("Please show us your health code and 72 test")

# logo()

# def add(x, y):
#     result = x + y
#     print(f"the result of {x} + {y} is {result}")

# add(114514, 520)
# add(1, 2)
# def add(a, b):
#     result = a + b
#     return result

# r = add(1, 2)
# print(r)
# def say_hi():
#     print("Hello")

# result = say_hi()
# print(f"{type(result)}")

# def check_age(age):
#     if age > 18:
#         return "success"
#     return None

# result = check_age(16)
# if not result:
#     print("under age, can not be permitted!")

# def add(x, y):
#     # x is the first parameter
#     # y is the second parameter
#     result = x + y
#     print(f"result is {result}")

# add(132, 12)

# def fun_b():
#     print("---b---")

# def fun_a():
#     print("---a---")

#     fun_b()

#     print("---c---")

# fun_a()

# def test_a():
#     num = 100
#     print(num)

# test_a()
# print(num)


# def test_a():
#     global num 
#     num = 500
#     print(f"test_a: {num}")

# test_a()
# print(num)

# money = 50000000
# name = None

# name = input("Please enter your name")

# def query():
#     print("----------------query the left----------------------")
#     print(f"{name}, hello, your money left is: {money} yuan")

# def saving(num):
#     global money
#     money += num
#     print("-----------Saving-------------")
#     print(f"{name}, hello, your saving{num} is successful")

#     query(False)

# def get_money(num):
#     global money 
#     money -= num
#     print("----------take money-----------")
#     print(f"{name}, hello, you take {money}")

# def main():
#     print("----------------money-------------")
#     print()

# while True:
#     keyboard_input = main()
#     if keyboard_input == '1':
#         query(True)
#         continue
#     elif keyboard_input == "2":
#         num = input("money:")
#         saving(num)
#     elif keyboard_input == '3':
#         num = int(input("enter: "))
#         get_money(num)
#         continue
#     else:
#         break

# name_list = ['itheima', 777, 'python']
# print(name_list)
# print(type(name_list))
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])
# print(name_list[-1])
# print(name_list[-2])
# print(name_list[-3])

# my_list = ["Tom", "Lily", "Rose"]
# list ---> vector
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])

# class Student:

#     def add(self, x, y):
#         return x + y

# student = Student()
# num = student.add(1, 2)
# print(num)
# mylist = ["itcast", "itheima", "python"]
# index = mylist.index("itheima")
# print(f"itheima in list index is: {index}")
# index = mylist.index("Hello")
# print(f"Hello in list index is: {index}")
# mylist[0] = "hello"
# print(mylist)
# mylist.insert(1, "best")
# print(mylist)
# mylist.append("linyiwei")
# print(mylist)
# mylist.extend([4, 5, 6])
# print(mylist)
# del mylist[2]
# print(mylist)
# element = mylist.pop(1)
# print(mylist)
# print(element)
# mylist.remove("itcast")
# print(mylist)
# mylist.clear()
# print(mylist)
# mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
# count = mylist.count("itheima")
# print(f"itheima: {count}")
# mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
# length = len(mylist)
# print(length)

# list = [21, 25, 21, 23, 22, 20]
# list.append(31)
# print(list)
# list.extend([29, 33, 30])
# print(list)
# print(list[0])
# print(list[-1])
# index = list.index(31)
# print(index)
# print(list)

# def list_while_func():
#     my_list = ["chuanzhijiaoyu", "heimachengxuyuan", "python"]
#     index = 0
#     while index < len(my_list):
#         element = my_list[index]
#         print(f"the element of the list: {element}")
        
#         index = index + 1

# list_while_func()

# def list_for_func():
#     my_list = [1, 2, 3, 4, 5]
#     for element in my_list:
#         print(f"the element is {element}")
    
# list_for_func()

# def list_while_func():
#     list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     even_list = []
#     i = 0
#     while i < len(list):
#         if (list[i] % 2 == 0):
#             even_list.append(list[i])
#         i += 1
#     print(f"This is the list: {list}, and this is the even list: {even_list}")

# list_while_func()

# def list_for_func():
#     nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     even_list = []
#     for num in nums:
#         if num % 2 == 0:
#             even_list.append(num)

#     print(f"This is the list: {nums}, and this is the even list: {even_list}")

# list_for_func()

# t1 = (1, "Hello", True)
# t2 = ()
# t3 = tuple()
# print(f"t1 type is {type(t1)}, {t1}")

# t5 = ((1, 2, 3,), (4, 5, 6))
# print(f"t5 type is {type(t5)}, {t5}")

# num = t5[1][2]
# print(num)

# t = ("chuanzhijiaoyu", "heimachengxuyuan", "Python", "linyiwei")
# index = t6.index("heimachengxuyuan")
# print(f"index: {index}")

# count = t6.count(t6)
# num = len(t6)

# print(f"t6 length is {num}")
# print(f"count is: {count}")

# index = 0
# while index < len(t):
#     print(f"the element in the tuple is: {t[index]}")
#     index += 1

# for element in t:
#     print(f"the element in the tuple is: {element}")

# t[0] = "list"
# t = (1, 2, ["list", "tuple"])
# print(f"{t}")
# t[2][0] = 1
# t[2][1] = "jasjfjsio" 
# print(t)

# name = "itheima"
# for x in name:
#     print(x)

# i = 0
# while i < len(name):
#     print(name[i], end = ' ')
#     i += 1
# name[1] = "H"
# print(name)

# value = name.index("ma")
# print(value)

# new_name = name.replace("it", "kajlsasfkkkkkkkkkkkkkkk")
# print(new_name)

# str = "hello python itheima itcast"
# list = str.split(" ")
# print(list)

#strip
# str = " itheima and itcast"
# newstr = str.strip(" ")
# print(str)
# print(newstr)
# print("I love you")

# str = "itheima and itcast"
# count = str.count("it")
# print(count)

# mystr = "itheima and itcast"
# num = len(mystr)
# print(num)

# mystr = "itheima itast boxuegu"
# count = mystr.count("it")
# print(count)
# str1 = mystr.replace(" ", "|")
# print(str1)
# list = str1.split("|")
# print(list)

#list chop
# list = [0, 1, 2, 3, 4, 5, 6]
# result1 = list[1:4]
# print(f"result1: {result1}")

# #tuple chop, from the beginning to the end
# tuple = (0, 1, 2, 3, 4, 5, 6)
# result2 = tuple[:]
# print(f"result2: {result2}")

# my_str = "01234567"
# result3 = my_str[::2]
# print(result3)

# result = my_str[::-1]
# print(result)

# result5 = mylist[3:1:-1]
# print(result5)

# result6 = tuple[::-2]
# print(result6)
# my_set = {"chuanzhijiaoyu", "heimachengxuyuan", "itheima","chuanzhijiaoyu", "heimachengxuyuan", "itheima"}
# set_empty =  set()
# print(my_set)
# print(set_empty)

# my_set.add("Python")
# my_set.add("chuanzhijiaoyu")
# print(my_set)

# my_set.remove("itheima")
# print(my_set)

# element = my_set.pop()
# print(element, "\n", my_set)

# my_set.clear()
# print(my_set)

# set1 = {1, 2, 3}
# set2 = {1, 5, 6}
# set3 = set1.difference(set2)
# print(set3)
# print(set1)
# print(set2)

# set1.difference_update(set2)
# print(set1)
# print(set2)

# print()

# set3 = set1.union(set2)
# print(set1)
# print(set2)
# print(set3)

# set1 = {1, 2, 3, 4, 5}
# num = len(set1)
# print(num)

# set1 = {1, 2, 3, 4, 5}
# for element in set1:
#     print(element)

# my_list = ["heimachengxuyuan", "chuanzhiboke", "heimachengxuyuan", "chuanzhiboke", "itheima", "itcast", "itheima", "itcast", "best"]
# my_set = set()
# for element in my_list:
#     my_set.add(element)
# print(my_set)
# print("I love you")

# my_dict = {"wanglihong":99, "zhoujielun": 88, "linjunjie": 77}

# # my_dict2 = {}
# # my_dict3 = dict()
# print(my_dict)
# # print(my_dict2)

# print(my_dict["wanglihong"])
# print(my_dict["zhoujielun"])
# print(my_dict["linjunjie"])
# print()

# score_dict = {
#     "wanglihong" : {
#         "Chinese" : 77,
#         "math" : 66, 
#         "english" : 33
#     } ,
#     "zhoujielun" : {
#         "Chinese": 88,
#         "math" : 86, 
#         "english" : 55  
#     } ,
#     "linjunjie" : {
#         "Chinese": 99,
#         "math" : 96, 
#         "english" : 66  
#     }
# }

# print(f"the information about this is {score_dict}")
# print(score_dict["zhoujielun"]["Chinese"])
# print(score_dict["wanglihong"]["Chinese"])
# print(score_dict["linjunjie"]["Chinese"])

# my_dict = {"zhoujielun": 99, "linjunjie": 88, "zhangxueyou": 77}
# print(my_dict)

# my_dict["zhangxinzhe"] = 66
# print(my_dict)

# my_dict["zhoujielun"] = 33
# print(my_dict)

# score = my_dict.pop("zhoujielun")
# print(f"{my_dict}")

# # my_dict.clear()
# # print("the dictionary has benn cleared.")

# keys = my_dict.keys()
# print(keys)
# for key in keys:
#     print(f"key is : {key}")
#     print(f"value is: {my_dict[key]}")

# num = len(my_dict)
# print(num)

# info_dict = {
#     "wanglihong" : {
#         "department" : "science",
#         "salary" : 3000,
#         "level" : 1
#     },
#     "zhoujielun" : {
#         "department" : "market",
#         "salary" : 5000,
#         "level" : 2
#     }, 
#     "linjunjie" : {
#         "department" : "market",
#         "salary" : 7000,
#         "level" : 3
#     },
#     "zhangxueyou" : {
#         "department" : "science",
#         "salary" : 4000,
#         "level" : 1
#     }, 
#     "liudehua" : {
#         "department" : "market",
#         "salary" : 6000,
#         "level" : 2
#     }
# }
# print(info_dict)

# for key in info_dict:
#     if (info_dict[key]["level"] == 1) : 
#         info_dict[key]["level"] += 1
#         info_dict[key]["salary"] += 1000    

# print(info_dict)
# print()

#sorted
# my_list = [1, 3, 5, 4, 2,]
# my_tuple = (3, 1, 2, 5, 4)
# my_str = "bdcefga"
# my_set = {3, 1, 2, 5, 4}
# my_dict = {"key3": 1, "key1": 2, "key2" : 3, "key5" : 4, "key4" : 5}

# print(f"the result of the list object is: {sorted(my_list)}")
# print(f"the result of the list object is: {sorted(my_tuple)}")
# print(f"the result of the list object is: {sorted(my_str)}")
# print(f"the result of the list object is: {sorted(my_set)}")
# print(f"the result of the list object is: {sorted(my_dict)}")
# print()

# print(f"the result of the list object is: {sorted(my_list, reverse = True)}")
# print(f"the result of the list object is: {sorted(my_tuple, reverse = True)}")
# print(f"the result of the list object is: {sorted(my_str, reverse = True)}")
# print(f"the result of the list object is: {sorted(my_set, reverse = True)}")
# print(f"the result of the list object is: {sorted(my_dict, reverse = True)}")

# print('abd' > 'abc')
# print('a' < 'A')

# def test_return():
#     return 1, 2, 3

# x, y, z = test_return()
# print(x, y, z)
# print(x)
# print(y)
# print(z)

# def user_info(name, age, gender):
#     print(f"Name: {name}, Age: {age}, Gender: {gender}")

# user_info(name = "xiaoming", age = 20, gender = "male")
# user_info(age = 20, gender = "male", name = "xiaoming")

# def user_info(name, age, gender = "male"):
#     print(f"Name: {name}, Age:")

# def user_info(*args):
#     print(args)

# user_info("Tom", 18, 114514, "json")

# def user_info(**kwargs):
#     print(kwargs)

# user_info(name = "Tom", age = 18, id = 110)

# def test_func(compute):
#     result = compute(1, 2)
#     print(result)

# def compute(x, y):
#     return x + y
# test_func(compute)
# def test_func(compute):
#     result = compute(5, 2)
#     print(result)
    
# test_func(lambda x, y: x + y)
# test_func(lambda x, y: x + y)
# test_func(lambda x, y: x + y)

# f = open("readme.txt", "r", encoding = "UTF-8")
# print(f.read(5))
# print(type(f))

# lines = f.readlines()
# print(lines)

# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# for i in range (0, 3):
#     print(f.readline())

# for line in f:
#     print(f"the data in the line is: {line}")

# f.close()
# import time
# with open("readme.txt", "r", encoding = "UTF-8") as f:
#     for line in f:
#         print(f"the data in the line is: {line}")

# time.sleep(5000000)

# file = open("word.txt", "r", encoding = "UTF-8")
# content = file.read()
# print(content)
# print(content.count("itheima"))

# count = 0
# for word in file:
#     print(word)
#     print()
#     if word == "itheima\0":
#         count += 1

# print(count)
# file.close()

# count = 0
# for line in file:
#     line = line.strip()
#     words = line.split(" ")
#     print(words)
#     for word in words:
#         if word == "itheima":
#             count += 1
# print(count)
# file.close()
# import time
# f = open('word.txt', 'w')
# f.write('lian')
# time.sleep(5000000)
# f.close()
# f.close()

# f = open("word.txt", 'a', encoding = "UTF-8")
# f.write("\nthe best choice for python")
# f.close()
# try:
#     f = open("error.txt", "r", encoding = "UTF-8")
# except:
#     print("the program has an error because of the nonexistence of the file, I will change to " \
#     "the w mode from the open mode to open the file")
#     f = open("error.txt", "w", encoding = "UTF-8")

# try:
#     # print(linyiwei) 
#     1 / 0
# # except NameError as e:
# except(NameError, ZeroDivisionError) as e:
#     print("the variable undefined error occured!")
#     print(e)

# try:
#     1 / 2
#     f = open("word.txt", "r")
# except Exception as e:
#     print("Errors occur")
# else:
#     print("there is no error in the program")
# finally:
#     print("there is a finally, whether there is a error I will perform")
#     f.close()

# def func1():
#     print("func1 begin to start")
#     num =  1 / 0
#     print("func1 execute finally")

# def func2():
#     print("func2 begin to start")
#     func1()
#     print("func2 end")

# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(f"error occured, info is {e}")

# main()
# import time
# from time import *
# sleep(5)

# import json
# data = [{"name": "zhangdashan", "age": 11}, {"name": "wangdachui", "age": 13}, {"name": "zhangxiaohu", "age": 16},]

# json_str = json.dumps(data)
# print(type(json_str))
# print(json_str)

# d = {"name": "zhoujielun", "addr": "taibei"}
# json_str = json.dumps(d)
# print(type(json_str))
# print(json_str)

# s = '[{"name": "zhangdashan", "age": 11}, {"name": "wangdachui", "age": 13}]'
# l = json.loads(s)
# print(type(l))
# print(l)

# d = '{"name": "zhoujielun", "addr": "taibei"}'
# json_str = json.loads(d)
# print(type(json_str))
# print(json_str)

# class Student:
#     name = None
#     gender = None
#     nationality = None
#     native_place = None
#     age = None
    
#     def say_hi(self):
#         print(f"hi everyone, my name is {self.name}")

#     def say_hi(self, msg):
#         print(f"hi everyone, this is {msg}")

# stu_1 = Student()
# stu_1.name = "linjunjie"
# stu_1.gender = "nan"
# stu_1.nationality = "zhongguo"
# stu_1.native_place = "shandongsheng"
# stu_1.age = "38"
# stu_1.say_hi("Linyiwei")

# class Clock:
#     id = None
#     price = None

#     def ring(self):
#         import winsound
#         winsound.Beep(2000, 3000)

# clock1 = Clock()
# clock1.id = "003032"
# clock1.price = 19.99
# print(f"clock id: {clock1.id}, price: {clock1.price}")
# clock1.ring()

# class Student:
#     name = None
#     # gender = None
#     # nationality = None
#     # native_place = None
#     age = None
#     tel = None
    
#     def __init__(self, name, age, tel):
#         self.name = name
#         self.age = age
#         self.tel = tel

#     def __str__(self):
#         return f"student: name: {self.name}, age: {self.age}"

#     def __lt__(self, other):
#         return self.age < other.age

#     def __le__(self, other):
#         return self.age <= other.age
    
#     def __eq__(self, other):
#         return self.age == other.age
    # def say_hi(self):
    #     print(f"hi everyone, my name is {self.name}")

    # def say_hi(self, msg):
    #     print(f"hi everyone, this is {msg}")

# stu = Student("zhoujielun", 31, "18500006666")
# print(stu.name)
# print(stu.age)
# print(stu.tel)
# print(stu)

# stu1 = Student("linjunjie", 36, "8328197859")
# print(stu1 > stu)
# print(stu1 < stu)

# print(stu1 > stu)
# print(stu1 < stu)

# class Phone:
#     IMEI = None
#     producer = None

#     __current_votage = 0.5

#     def __keep_single_core(self):
#         print("let cpu single run")

#     def call_by_5g(self):
#         if self.__current_votage >= 1:
#             print("5g is on")
#         else:
#             print("5g is off")
#             self.__keep_single_core()
# phone1 = Phone()
# # phone1.__keep_single_core()
# phone1.call_by_5g()

# class Phone:
    
#     __is_5g_enable = False

#     def __init__(self):
#         self.__is_5g_enable = True

#     def __check_5g(self):
#         if self.__check_5g == True:
#             print("5G is on")
#         else:
#             print("5G is off, 4G is using")
        
#     def call_by_5g(self):
#         self.__check_5g()
#         print("is on the phone")

# ios_phone = Phone()
# ios_phone.__init__()
# ios_phone.call_by_5g()

# class Phone:
#     IMEI = None
#     producer = None

#     def call_by_4g(self):
#         print("4g telephone")
# class Phone2022(Phone):
#     face_id = True

#     def call_by_5g(self):
#         print("2022 latest 5g telephone")

# ios_phone = Phone2022(Phone)
# print(ios_phone.producer)
# ios_phone.call_by_4g()
# ios_phone.call_by_5g()


# class Phone:
    
#     __is_5g_enable = False

#     def __init__(self):
#         self.__is_5g_enable = True

#     def __check_5g(self):
#         if self.__check_5g == True:
#             print("5G is on")
#         else:
#             print("5G is off, 4G is using")
        
#     def call_by_5g(self):
#         self.__check_5g()
#         print("is on the phone")

# class NFCReader:
#     nfc_type = "the fifth generation"
#     producer = "HM"

#     def read_card(self):
#         print("NFC reader")
    
#     def write_card(self):
#         print("NFC write card")

# class RemoteControl:
#     rc_type = "infrared control"

#     def control(self):
#         print("infrared control is on")

# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass

# phone = MyPhone()
# phone.call_by_5g()
# phone.read_card()
# phone.write_card()
# phone.control()

# class Phone :
#     IMEI = None
#     producer = "ITCAST"
#     def call_by_5g(self):
#         print("using 5G network to phone")

# class MyPhone(Phone):
#     producer = "ITHEIMA"

#     def call_by_5g(self):
#         print("CPU on and make sure less electricity")
#         print("using 5G to phone")
#         print(Phone.producer)
#         print(super().producer)
#         print("5G is off and make sure the performance")

# phone = MyPhone()
# phone.call_by_5g()
# print(phone.producer)

# import random 
# print(random.randint())

# var_1 : int = 10
# var_2 : str = "itheima"
# var_3 : bool = True

# class Student:
#     pass
# stu : Student = Student()

# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = ["linyiwei", "18"]

# var_1 = 10    # type: int

# def add(x: int, y: int):
#     return x + y
# print(add(12, 12))

# def func(data: list) -> list:
#     return data
    
# print(func([1, 2, 3]))

# my_list: list[int] = [1, 2, 3]
# my_dict: dict[str, int] = {"age": 11, "num": 3}

# from typing import Union

# my_list: list[Union[str, int]] = [1, 2, "itcast", "itheima"]

# # my_dict: dict[str, Union[str, int]] = 

# def func(data: Union[int, str]) -> Union[int, str]:
#     pass

# func()

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print("wangwangwang")

# class Cat(Animal):
#     def speak(self):
#         print("miaomiaomiao")

# def make_noise(animal: Animal):
#     animal.speak()

# dog = Dog()
# cat = Cat()

# make_noise(dog)
# make_noise(cat)

# class AC:
#     def cool_wind(self):
#         "cold"
    
#     def hot_wind(self):
#         pass

#     def swing_l_r(self):
#         pass

# class Midea_AC(AC):
#     def cool_wind(self):
#         print("midea cold wind")
    
#     def hot_wind(self):
#         print("midea hot wind")

#     def swing_l_r(self):
#         print("Midea wind")

# class GREE_AC(AC):
#     def make_cool(ac: AC):
#         print("gree cold wind")

#     def hot_wind(self):
#         print("gree hot wind")

#     def swing_l_r(self):
#         print("gree swing wind")

# def make_cool(ac: AC):
#     ac.cool_wind()

# midea_ac = Midea_AC()
# gree_ac = GREE_AC()

# make_cool(midea_ac)
# make_cool(gree_ac)



