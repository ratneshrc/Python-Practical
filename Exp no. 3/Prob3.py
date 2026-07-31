n = input("Enter string:")
rev = " "

for i in range (len(n)-1,-1,-1):
     rev +=n[i]
    
print(rev)