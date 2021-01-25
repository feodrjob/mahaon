k=0
with open('Perepis.txt','r+') as f:
    for i in f:
        print(i)
        i=int(i[-5:])
        print (i)
        if i<1978:
            k+=1
print(k)

print('haha')