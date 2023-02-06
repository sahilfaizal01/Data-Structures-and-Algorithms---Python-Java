a = 14
b = 2
c = 12
if((a>b and b>c)or(c<a and a<b)):
    print('c is smallest')
elif((b>a and c>a)or(a<b and b<c)):
    print('a is smallest')
elif((c>a and a>b)or(a>c and c>b)):
    print('b is smallest') 
