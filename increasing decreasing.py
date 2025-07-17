def increasingdecreasing(n,num):
    
    if n < 1 or n > num:
        return
    print (n)
    increasingdecreasing(n-1,num)
    print (n)
    
n = int(input("Enter the n : "))
increasingdecreasing(n,n)