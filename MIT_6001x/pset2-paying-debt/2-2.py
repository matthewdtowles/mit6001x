'''
write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month
'''

payment = 10
i = 0
while i < 12:
  if i == 0:
    unpaid = balance - payment
  else:
    unpaid = unpaid + unpaid*(annualInterestRate/12) - payment
  i += 1
  # after 12 payments
  if i == 12:
    # if money still owed, reset balance, counter, increase payment 
    if unpaid > 0:
      unpaid = balance
      i = 0
      payment += 10
    else:
      print('Lowest Payment: '+str(payment))