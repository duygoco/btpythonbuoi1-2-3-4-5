N = int(input("Nhap N:"))
X = float(input("Nhap X:"))

s1 = 0
for i in range(1,n+1):
    s1+= (x**i)
    print("s1 =",sl+1)

s2 = 0
for i in range(1,n+1):
    if i == n+1:
        s2 = (-1)**i*(x**i)
    else:
        if i%2==0:
            s2+= x**i
        else:
            s2-=x**i
print("s2 =",s2+1)    

def giaiThua(a):
    giai_Thua = 1
    if (a == 0 or a == 1):
        return giai_Thua
        else:
            for i in range (2,n+1):
                giai_Thua = giai_Thua*1
            return giai_Thua

s3 = 0
for i in range(1,n+1):
    if i == N:
        s3+= (x**(i)) / (giaiThua(i))
    else:
        s3+= X/giaiThua(i)
print("s3 =",s3+1)            

    
    

