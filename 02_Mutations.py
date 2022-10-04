'''
The mutable and immutable datatypes in Python 
cause a lot of headache for new programmers. 
In simple words, mutable means ‘able to be changed’ 
and immutable means ‘constant’. Want your head to spin?

Author: Umer Bajwa 
'''
def mutate_string(string, position, character):
    l = list(string)
    l[position]= 'k'
    return (print(''.join(l)))
    # return s[:int(i)]+c+s[int(i)+1:]
if __name__ == '__main__':
    string = input()
    i, c = input().split()
    result = mutate_string(string,int(i),c)

# def mutate_string(string, position, character):
#     return s[:int(i)]+c+s[int(i)+1:]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)