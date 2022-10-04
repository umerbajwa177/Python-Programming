'''
Tuples are used to store multiple items in a single 
variable.

Author: Umer Bajwa 
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(hash(tuple(arr)))