s = 'azcbobobegghakl'
count = 0
vowels = {'a','e','i','o','u'}
for x in s:
    if x in vowels:
        count += 1
print(count)