'''
find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year
'''

def unpaid(bal,payment,intRate):
    for m in range(12):
        bal -= payment
        bal *= (1+(intRate/12))
    return bal
def pmt(hi,lo):
    return (hi+lo)/2
monthlyInterestRate = annualInterestRate/12
low = balance/12
high = (balance*(1+monthlyInterestRate)**12)/12
payment = pmt(high,low)
unpaidBal = unpaid(balance,payment,annualInterestRate)
while(round(unpaidBal,2) != 0):
    if unpaidBal > 0:
        low = payment
    else:
        high = payment
    payment = pmt(high,low)
    unpaidBal = unpaid(balance,payment,annualInterestRate)
print("Lowest payment: %.2f" % payment)