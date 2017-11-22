vowels = ['a','e','i','o','u']
n = 0
for t in s:
    if (t in vowels):
        n += 1
print('Number of vowels: '+ str(n))