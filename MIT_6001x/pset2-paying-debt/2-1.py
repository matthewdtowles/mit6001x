'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
'''

i = 0;
while i <= 12:
  if(i == 0):
    unpaid = balance - (balance*monthlyPaymentRate)
  else:
    balance = unpaid + (unpaid*(annualInterestRate/12))
    unpaid = balance - (balance*monthlyPaymentRate)
  i += 1
print("Remaining balance: %.2f" % balance)