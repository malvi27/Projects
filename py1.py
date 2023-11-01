num=int(input("enter"))
c=s=d=0
n=num
while num:
        num=num//10
        d+=1
num=n        
while num:
        c=num%10
        s=s+c**d
        num=num//10
if (s==n):
        print("armstrong")
        
                        
