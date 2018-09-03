# Python3
# Problem Statement: https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
    leap = False
    
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        leap = True
    
    return leap
