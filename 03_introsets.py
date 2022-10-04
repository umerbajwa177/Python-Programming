'''
Author: Umer Bajwa 

Basically, sets are used for membership testing and eliminating duplicate entries.
'''
def average(array):
    # your code goes here
    s= set(array)
    return sum(s)/len(s)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)