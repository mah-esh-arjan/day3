id_lst=[]
name_lst=[]
add_lst=[]
for i in range (3):
    id = int(input('enter your id: '))
    id_lst.append(id)
    name = input('enter your name:')
    name_lst.append(name)
    add = input('enter your adress: ')
    add_lst.append(add)
for i in range (3):
    print(f'id:{id_lst[i]} name:{name_lst[i]} add:{add_lst[i]}')
