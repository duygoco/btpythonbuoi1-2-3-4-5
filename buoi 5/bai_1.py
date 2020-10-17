def input_data(n):
    list=[]
    for i in range(1,n+1):
        list.append(int(input(f"Phần tử thứ[i]:")))
    return list
n=int(input("Nhập:"))
print(input_data(n))        

def input_data(n):
    b=[]
    i=0
    while True:
        x = input(f"Phần tử thứ[{i}]: ")
        try:
         b.append( int(x))
         i+=1
         if i>= n:
            break
        except: 
         print("Chưa nhập đúng số nguyên . Nhập lại")    

    return b


#Tính tổng của mảng 1 chiều
def tinh_tong(b):
    a= input_data(n)
    tong=0
  for i in a:
    sum = sum +1
    print(sum)
       
