bin=input()
bin=bin[::-1]
dec=0
for i in range(len(bin)):
    digit=int(bin[i])
    power=2**i
    res=digit*power
    dec=dec+res
print(dec)
