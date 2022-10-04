'''
Author: Umer Bajwa 

'''
m=int(input())
list1=list(map(int,(input().split())))
n=int(input())
list2=list(map(int,(input().split())))
set1=set((list1))
set2=set(list2)
a=set1.difference(set2)
b=set2.difference(set1)
c=a.union(b)
c=sorted(c)
for x in c:
    print(x)