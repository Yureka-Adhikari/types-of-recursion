def negative():
    n = int(input("Enter a number: "))
    if n < 0:
        print(n)
        return
    else:
        print(n)
        negative()
        
negative()