num = int(input('enter any num ='))
list= []
for i in range(0,num+1):
    if i%2 !=0:
        list.append(i)
print(list)


a = [x for x in range(int(input('enter  any num=')))if x%2!=0 ]
print(a)