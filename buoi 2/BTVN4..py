a = int(input("Nhap a :"))
b = int(input("Nhap b :"))
c = int(input("Nhap c :"))
if(a<c+b and b<a+c and c<a+b):
    if(a*a==b*b+c*c or b*b==a*a or c*c==a*a+b*b):
        print (" tam giac vuong")
    else:
        print("khong phai tam vuong")

else :
    print("khong phai tam giac vuong")            
