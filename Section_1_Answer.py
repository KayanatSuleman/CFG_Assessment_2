'''1.7 Looking at the following code, describe a case where 
this function would throw an error when called? [5 mark]'''

def can_pay(price, cash_given):
  if cash_given >= price:
    return True
  else:
    return False

print(can_pay(50, 20))

'''
This code would throw an error if one or both of the integers are strings.
This particular code does not account for the possibility of accepting 
a string. Although it would be impractical to enter a string when dealing
with numbers. To mitigate this TypeError we can implement 
exception handling using a try - except block in the function. This is 
demonstrated below.
'''

def can_pay(price, cash_given):
 try:
  if cash_given >= price:
    return True
  else:
    return False

 except TypeError:
   print("Error, Both price and cash_given must be a integer.")
   return

print(can_pay(20.00, "50"))

'''
As shown above, if a string is passed as one of the arguments, 
it is caught by the try - except exception handling, and outputs an 
error message for an easier way to debug and identify what has gone wrong.
'''