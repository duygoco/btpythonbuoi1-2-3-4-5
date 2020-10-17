n = int(input("nhap n la so nguyen duong [1->1000]:"))
while (n>999 or n < 0:)
(input("Nhap lai n la so nguyen duong [1->1000]:"))
sum=0
while (n>0):
    sum = sum + n % 10
    n = int ( n / 10 )
print(sum)    
