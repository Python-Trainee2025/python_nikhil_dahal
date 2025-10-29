# ##help('keywords')
#
#
# a=2
# b=3
# c=a+b
# print(c)
#
# a=5
# if a==2:
#     print('true')
# elif a<2:
#     print('false')
# else:
#     print('nothing')
#
#
# i=input('enter:')
# print(i)
# j=int(input('enter:'))
# print(j)
# name='nikhil'
# age=22
# print("name",name,"age",age)
# print("name is {} and age is {}".format(name,age))
# print(f"name is {name} age is {age}")

# # a='madam'
# print(a[1])#indexing
# print(a[1:3])#slicing
# # print(a[::-1])#reverse string



# a=' cat is   '
# # print(a.lower())
# # # print(a.upper())
# # print(a.strip())#remove white space
# print(a. replace('cat','dog'))# replace strings
#
#
# a= 'helo, my name is nikhil'
# # s=a.split(' ')
# # b=a.split(',')
# # print(s+b)
# # j=''.join(a)
# # print(j)
# print(a.endswith('l'))
# print(a.startswith('a'))
# # print(a.isalpha)
# print(a.count('i'))
# print(len(a))
#basic tuples list:
# list:l=[1,2,3,4,5]
# tuple:t:(1,2,3,4,5)
# dict:{'a':1,'b':2}
# set:s={1,2,3,4,5}


#
# ip=input('enter values seperated by a space:').split(',')
# print(ip)


# income,tax=input('enter your income and tax rate: ').split(',')
# total = int(income) * int(tax)
# print(total)

# ip=list((map(float,input('Enter income and tax rate: ').split(','))))
# total=ip[0]*ip[1]
# print(total)

###########################################

# a=[1,2,3,4,5]
# for i in a:
#     if i%2==0 :
#         print('inside the loop',i)
#     else:
#         print('outside the loop',i)

######range
# for i in range(1,50):
#     if i % 2 == 0:
#       print('inside the loop',i)

######step
# for i in range(0,10,2):
#     if i % 2 == 0:
#          print('inside the loop',i)

######while loop
# c=['apple','banana','orange']
# while c[0]!='orange':
#     print(c)
#     c+=1


#######forloop


# num = int(input("Enter a number: "))
# if num >= 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")



#basic function
# def greet():
#     print('Hello')
#
# greet()

# #function with parameter
# def add(a,b):
#     return a+b
# result=add(3,4)
# print(result)

#default parameter
# def greet(name='Guest'):
#     print('Hello',name)
# greet()
# greet('Jim')
#
# #named arguments
# def add(*args):
#     total=0
#     for num in args:
#         total+=num
#     return total
# print(add(1,2,3))

#keyword arguements
# def info(**kwargs):
#     for key,value in kwargs.items():
#         print(f'{key} = {value}')
# info(name='Jim',age=25,city='ktm')



##############################################################

# def fact(n):
#     res=1
#     for i in range(1,n+1):
#         res=res*i
#     return res
# print(fact(5))

# def rec_funct(n):
#     if n==1:
#         return 1
#     else:
#         return n*rec_funct(n-1)
#
# print(rec_funct(5))


# sq=lambda x:x*x
# print(sq(10))
#
# max=lambda a,b:a if a>b else b
# print(max(10,5))



##########################################
#file handling

# file=open('first_file.txt','w')
# file.write("Hello World")
# file.close()
#
# file=open('first_file.txt','r')
# data=file.read()
# print(data)


