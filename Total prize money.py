# cook your dish here
a = int(input())
for i in range(a):
    c=[]
    b=input()
    c=b.split(" ")
    c=list(map(int,c))
    print(c[0]*10 + c[1]*90)