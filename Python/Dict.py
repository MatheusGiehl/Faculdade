# 4 maneiras de uso 

#I
dici_1 = {}

dici_1['name'] = 'Maria'
dici_1['age'] = 25

print(dici_1)

#II
dice_2 = {'name' : 'João', 'age': 28}

print(dice_2)

#III
dice_3 = dict(name = 'Lucas', age = 35)

print(dice_3)

#IV
dice_4 = dict(zip(['name', 'age'], ['Pedro', 33]))
print(dice_4)


# ALTERANDO VALORES

produto = dict(zip(['product', 'price', 'quantity'], ['Som', 3000, 10])) 

print(produto)

#Alterando Estoque
produto['quantity'] = 8
print(produto)