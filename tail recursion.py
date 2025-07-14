def tail(n,num):
    if n < num:
        return
    print(n)
    tail(n-1, num)
    
n = int(input("Enter the number to count from n to 1 : "))
tail(n,1)