a = 100
b = 200
s=0
#in our range from 100 to 200 inclusive, if a number is odd, we add it to the count
for i in range (a, b+1):
    if not i%2==0:
      s=s+i

print s

