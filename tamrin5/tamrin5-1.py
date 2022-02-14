
def pascal(n):
    s=[]    
    lst=[]
    for i in range(n):
        if i == 0:
            lst.append(1)
            print(lst)
            lst.clear()
        elif i==1:
            lst.append(1)
            lst.append((1))
            s=lst.copy()
            print(lst)
            lst.clear()
        elif 2<= i <=n:
            lst.append(1)
            for j in range(1,i):
                lst.append(s[j]+s[j-1])
            lst.append(1)
            s=lst.copy()
            print(lst)
            lst.clear()
pascal(10)        
