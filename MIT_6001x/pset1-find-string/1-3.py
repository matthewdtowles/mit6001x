'''
Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
'''

sub1 = s[0]
sub2 = ''
i = 0
for t in s[:-1]:
    if(s[i] <= s[i+1]):
        sub1 += s[i+1]
    elif(s[i] > s[i+1]):
        if(len(sub1) > len(sub2)):
            sub2 = sub1
        sub1 = s[i+1]
    i += 1
if(len(sub1) > len(sub2)):
    substring = sub1
else:
    substring = sub2
print('Longest substring in alphabetical order is: '+substring)