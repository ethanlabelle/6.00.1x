s = 'azcbobobegghakl'
longest = ''

for i in range(len(s)):
    start = i
    count = 1
    while start + count < len(s) and s[start] <= s[start + count]:
        start = start + count 
    if len(s[i:start+count]) > len(longest):
        longest = s[i:start + count]

print('Longest substring in alphabetical order is:', longest)