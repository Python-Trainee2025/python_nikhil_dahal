
# Question no.1

num=int(input('Enter a number: '))
a,b=0,1
result=[]
for _ in range(num):
    result.append(a)
    a,b=b,a+b
print(result)



num=int(input('Enter a number: '))
def rec_num(n):
    if n<=1:
        return n
    else:
        return rec_num(n-1)+rec_num(n-2)
result=[rec_num(i) for i in range(num)]

print(f'The fibonacci series of {num} is: {result}')


# Question no.2

word=input('Enter a word or sentence: ')
vowels=['a','e','i','o','u']
for vowel in vowels:
    print(f'The total number of {vowel} vowels is: {word.count(vowel)}')


# Question no.3

with open('assignment_file.txt','w') as file:
    file.write('This is my second assignment of python in my training in Infinite.')

def count_word_in_file(assignment_file):
    try:
        with open('assignment_file.txt','r') as file:
            word=file.read()
            count_word=word.split()
            print(f'The total word count is: {len(count_word)}')
    except FileNotFoundError:
        print('The file was not found.')

count_word_in_file('assignment_file')


#Question no.4
def rec_calc():
    num=int(input('Enter first number: '))
    num2=int(input('Enter second number: '))
    print('Which operation would you like to perfrom:\n Type 1 for Addition.'
      '\n Type 2 for Subtraction.\n Type 3 for Multiplication.\n Type 4 for Division.')
    choose=int(input('Enter your choice: '))
    if choose==1:
        print('The addition of two given numbers are: ',num+num2)
    elif choose==2:
        print('The subtraction of two given numbers are: ', num-num2)
    elif choose==3:
        print('The multiplication of two given numbers are: ', num*num2)
    elif choose==4:
            if num2!=0:
                print('The division of two given numbers are: ', num / num2)
            else:
                print('Division by zero is not allowed!')
    else:
        print('Invalid choice')

    again = input("Do you want to perform another operation?\n Y for Yes \n N for No \n-> ").lower()
    if again == "y":
        rec_calc()
    else:
        print("Calculator exited!")

rec_calc()


#Question no.5

import csv
def read_csv_file(data):
    try:
        with open(data, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{data}' was not found.")
    except csv.Error as e:
        print(f"CSV parsing error: {e}")

read_csv_file('data.csv')
