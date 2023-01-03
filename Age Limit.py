# cook your dish here
a= int(input())
for i in range(a):
    c=[]
    b= input()
    c= b.split(" ")
    c=list(map(int, c))
    if c[0]<=c[2]<c[1] :
        print("YES")
    else :
        print("NO")