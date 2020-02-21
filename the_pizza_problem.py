total,pizza=0,0
with open('d_quite_big.in','r') as f:
    f_contents = f.readline()
    total,pizza = map(int,f_contents.split(' '))
    f_contents = f.readline()
    slices=list(map(int,f_contents.split(' ')))


req=0
req_pizza=[]
for j,i in enumerate(slices[::-1]):
    if req + i < total:
        req+=i
        req_pizza.append(str(len(slices)-j-1))
        slices[len(slices)-1-j]='a'
    else:
        continue


with open('output_quite_big.txt' , 'w') as f:
    f.write(str(len(req_pizza))+'\n')
    f.write(' '.join(req_pizza[::-1]))
