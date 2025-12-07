#!/usr/bin/env python3

def happy_new_year():
    """
    Count down from 10 to 1 and print 'Happy New Year!'
    """
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    """
    Return a list of squared integers from the input list.
    
    Args:
        int_list (list): A list of integers
    
    Returns:
        list: A list of squared integers
    """
    return [num * num for num in int_list]

def fizzbuzz():
    """
    Print numbers from 1 to 100 following FizzBuzz rules:
    - For multiples of 3, print "Fizz"
    - For multiples of 5, print "Buzz"
    - For multiples of both 3 and 5, print "FizzBuzz"
    - Otherwise, print the number
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)