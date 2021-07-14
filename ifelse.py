n = int(input())
if(n%2==0):
    if(n>=2 and n<4):
        print('Not weird')
    elif(n>=6 and n<=20):
        print('Weird')
    else:
        print('Not Weird')
else:

    print('Weird')