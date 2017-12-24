# how to round a float number to 2 decimal places,
# and output that number as $ currency
# print with a comma after the number of thousands.
#
# i.e print 1234.5678 as $1,234.57

number = 1234.5678
print (number)
number = round(number,2)
print (number)

# the above line rounds the number to 2 decimal places
thousands = number / 1000
print (thousands)
thousands = int(thousands)
print (thousands)
remainder = number % 1000
print (remainder)
pretty_output = "$" + str(thousands) + "," +str(remainder)
print (pretty_output)