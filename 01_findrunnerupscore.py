'''
Author: Umer Bajwa 
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    #print(list(set(arr)))
    print(sorted(list(set(arr)))[-2])
