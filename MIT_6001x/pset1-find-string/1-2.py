'''
Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
'''

start = 0
end = 3
count = 0
for t in s:
    if(s[start:end] == 'bob'):
        count += 1
    start += 1
    end += 1
print('Number of times bob occurs is: '+str(count))