'''
Author: Umer Bajwa 
'''
def main():
    # Replace all ______ with rjust, ljust or center. 

    s = int(input())  # This must be an odd number
    c = 'H'
    
    # Top Cone
    for i in range(s):
        print((c * i).rjust(s - 1) + c + (c * i).ljust(s - 1))
    
    # Top Pillars
    for i in range(s+1):
        print((c * s).center(s * 2) + (c * s).center(s * 6))
    
    # Middle Belt
    for i in range((s + 1) // 2):
        print((c * s * 5).center(s * 6))    
    
    # Bottom Pillars
    for i in range(s + 1):
        print((c * s).center(s * 2) + (c * s).center(s * 6))    
    
    # Bottom Cone
    for i in range(s):
        print(((c * (s - i - 1)).rjust(s) + c + (c * (s - i - 1)).ljust(s)).rjust(s * 6))  

if __name__ == '__main__':
    main()