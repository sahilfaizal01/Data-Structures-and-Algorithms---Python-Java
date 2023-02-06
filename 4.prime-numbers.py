a =13
flag = 0
if a == 2:
    print('Prime')
else:
    for i in range(2,a//2):
        if(a%i==0):
            flag = 1
    if(flag==1): 
        print('Not prime')
    else:
        print('prime')
    
