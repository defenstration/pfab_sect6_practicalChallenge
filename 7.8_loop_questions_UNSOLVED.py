#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 08:50:32 2019

@author: Giles
"""

'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
def counter():
    #Gather user inputs
    user_input_1 = int(input('Please input a number between 1 and 100: '))
    user_input_2 = int(input('Please input a second number between 1 and 100: '))
    #Count from lower to higher number
    if user_input_1 < user_input_2: 
        while user_input_1 < user_input_2 +1:
            print(user_input_1)
            user_input_1 += 1
    elif user_input_1 > user_input_2:
         while user_input_1 + 1 > user_input_2:
             print(user_input_2)
             user_input_2 += 1
        
    

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
def reverse_input():
    user_input_str = str(input('Please enter a value to reverse: '))
    user_input_list = [*user_input_str]
    reversed_list = user_input_list[::-1]
    reversed_str = ''.join(reversed_list)
    print(reversed_str)
    
#txt = 'jungle'
#splt = txt.split()
#print([*txt])



'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
def times_table():
    #Get user input
    times_table_user_input = int(input('Please enter a value between 1 and 12: '))
    times_table_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #Generate times table
    for num in times_table_list:
        print(num * times_table_user_input)

'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
def times_table_map():
    #Define varaibles
    new_times_table = []
    times_table_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #generate table
    for num in times_table_list:
         for number in times_table_list:
            new_times_table.append(num * number)
            print(new_times_table[-1])


'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''

def find_mean():
    #Define Variables
    mean_user_input = input('Please input a sequence of numbers: ')
    mean_user_list = mean_user_input.split()
    mean_user_list_number = []
    #Change to integers
    for seq in mean_user_list:
        mean_user_list_number.append(int(seq))
    #Generate mean    
    total = sum(mean_user_list_number)
    mean = total / len(mean_user_list_number)
    print(mean)

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''

def fifteen_factorial():
#    factorial_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    #Define Variables
    total = 1
    i = 1
    #Generate factorial
    while i < 15:
        total = total + i * total
        i+=1
    print(total)
        

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
def fibonacci():
    # Define Variables
    fibonacci_list = []
    i = 0
    # Generate Fibonacci sequence
    while i < 20:
        if i == 0:
            fibonacci_list.append(i)
            i+=1
        elif i==1:
            fibonacci_list.append(i)
            i+=1
        else:            
            num = fibonacci_list[i-2] + fibonacci_list[i-1]
            fibonacci_list.append(num)
            i+=1
    print(fibonacci_list)
        


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

def star_drawing():
    # Produce Variables
    star = '*'
    list_of_star_numbers = [5, 1, 4, 1, 1, 1]
    # Create drawing 
    for num in list_of_star_numbers:
        print(num * star)

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

def odds_and_evens():
    list_to_hundred = []
    odds_list = []
    evens_list = []
    # Create list of numbers to 100     
    i = 1
    while i <= 100:
        list_to_hundred.append(i)
        i+=1
#    print(list_to_hundred)
    # Add numbers to odds and evens lists   
    for num in list_to_hundred:
        if num%2 == 0:
            evens_list.append(num)
        elif num%2 != 0:
            odds_list.append(num)
            
    print(evens_list)
    print(odds_list)





























