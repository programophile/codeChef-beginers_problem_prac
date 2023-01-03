# cook your dish here
num_of_case= int(input())
for i in range(num_of_case) :
    c=[]
    b=input()
    c=b.split(" ")
    c=list(map(int,c))
    d= max(c)
    c.remove(d)
    print(max(c))