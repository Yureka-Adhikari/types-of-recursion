def head(n,num):
    if n > num:
        return
    print(n)
    head(n+1, num)
    
n = int(input("Enter the number to count from 1 to n : "))
head(1,n)