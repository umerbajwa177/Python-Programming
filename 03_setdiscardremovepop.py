'''
Author: Umer Bajwa 

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int,input().split()))
for _ in range(int(input())):
    o =input().split()
    
    if o[0] == 'pop':
        s.pop()
    elif o[1] == 'remove':
        s.remove(int(o[1]))
    else:
        s.discard(int(o[1]))
      
print(sum(s))