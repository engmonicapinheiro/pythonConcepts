numero = int(input("Digite o valor de n: "))

temp = numero
soma = 0

while numero != 0:
    algarismo = numero % 10
    soma = soma + algarismo
    numero = numero // 10

print(soma)






