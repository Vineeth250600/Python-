def Even_or_Odd(n):
    if(n%2!=0):
        print('Weird')
    elif(n%2==0 and 2<=n<=5):
        print('Not Weird')
    elif(n%2==0 and 6<=n<=20):
        print('Weird')
    elif(n%2==0 and n>20):
        print('Not Weird')

a=int(input())
Even_or_Odd(a)  


    



