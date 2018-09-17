a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
# Verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))
