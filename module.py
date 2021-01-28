k=0
a=int(input('diapazon'))
b=int(input('diapazon2'))

with open('Perepis.txt','r+') as f:
    for i in f:
        #print(i)
        x=int(i[-5:])
        #print (x)
        l=i.split()
        if(a<x<b):
            k=k+1
            print(l[1],l[2],l[3])


print(k)


