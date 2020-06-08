word = 'bob'
count = 0
for i in range(len(s) - 2):
  if (s[i:i+3] == word):
    count += 1
  #print(s[i:i+3])
print('Number of times bob occurs is: %d' % count)
