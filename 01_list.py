'''
Author: Umer Bajwa 
'''
if __name__ == '__main__':
    x = []
    n = int(input())
for i in range(n):
    a = input().split()
    if len(a) == 3:
        eval("x." + a[0] + "(" + a[1] + "," + a[2] + ")")
    elif len(a) == 2:
        eval("x." + a[0] + "(" + a[1] + ")")
    elif a[0] == "print":
        print(x)
    else:
        eval("x." + a[0] + "()")