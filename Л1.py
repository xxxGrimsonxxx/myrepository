a=input()
b=input()
c=input()
d=int(b)**2-4*int(a)*int(c)
if int(d) >0:
    x1=(-int(b)+d**0.5)/2*int(a)
    x2=(-int(b)-d**0.5)/2*int(a)
    print(x1, x2)
if int(d)== 0:
    x1=-int(b)/2*int(a)
    print(x1)
if int (d)<0:
    print ("корней нет")
    
