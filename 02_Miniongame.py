'''
Author: Umer Bajwa 

'''
def minion_game(string):
    # your code goes here
    s=len(string)
    c,v=0,0
    for i in range(s):
        if string[i] in 'AIEOU':
            v=v+(s-i)
        else:
            c=c+(s-i)
    if c>v:
        print("Stuart {}".format(c))
    elif c==v:
        print('Draw')
    else:
        print('Kevin {}'.format(v))

if __name__ == '__main__':
    s = input()
    minion_game(s)