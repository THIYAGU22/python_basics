def checkPrime(a,flag):
    for x in range(2,a/2):
        if(a%x==0):
            flag = 1
            break

    if(a==1):
        print(a,"is a prime number")

    if(flag == 1):
        print("not a prime number")
    else:
        print("it is a prime number")


inp = input()
#checkPrime(inp,0)

