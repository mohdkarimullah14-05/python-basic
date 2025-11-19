n1,n2,n3 = map(int,input("Enter three numbers : ").split())
res = 0
if n1 > n2 and n1 > n3:
    res = n1
elif n2 > n1 and n2 > n3:
    res = n2
else:
    res = n3
print("Largest among given three nums : ",res)