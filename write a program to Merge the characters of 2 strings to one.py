#Merge the characters of 2 strings to one
s1 = input()
s2=input()
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j +1
print(output)
