
#Definindo conjunto
meu_conjunto = set()

#Valores iguais não se repetem no conjunto
meu_conjunto.add(20)
meu_conjunto.add(40)
meu_conjunto.add(60)
meu_conjunto.add(40)

print(meu_conjunto)

#Criando variável e verificando se ela pertence ao meu conjunto !
valor = 20

if valor in meu_conjunto :
    print(f"O Valor : {valor} está no conjunto")
else :
    print(f"O valor : {valor} não está no conjunto")