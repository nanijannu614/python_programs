n=int(input()) 
bin=[] 
while n>0:
    bin.append(n%2)
    n=n//2
    bin.reverse() 
for i in bin:
    print(i,end=" ")
