# cook your dish here
ttst_case = int(input())
for i in range(ttst_case):
    list1=[]
    times= input()
    list1=times.split(" ")
    list1=list(map(int,list1))
    print(((180+list1[0])*2)-(list1[1]+list1[2]))