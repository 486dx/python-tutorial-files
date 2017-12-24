################################################################
#                                                              #
# 02-02.py                                                     #
# Purpose: to demonstrate storage of a floating point number   #
#                                                              #
# Programmer: Anne Dawson                                      #
# Last updated: Sunday 21st March 2010, 12:45 PT               #
#                                                              #
# See this resource to find out how the input function works:  #
# http://www.annedawson.net/Python3_Input.txt                  #
#                                                              #
# See this resource to find out how important comments are:    #
# http://www.annedawson.net/PythonComments.txt                 #
#                                                              #
################################################################

number1=float(input("Enter the first number: "))
number2=float(input("Enter the first number: "))
number3=float(input("Enter the third number: "))
total = number1 + number2 + number3
average = total / 3
print ("The average is: ")
print (average)