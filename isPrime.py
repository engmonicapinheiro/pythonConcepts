number = int(input("Digite um número inteiro: "))
i = 2
isPrime = True
while i < number:
    if number % i == 0:
        isPrime = False
    i = i + 1

if isPrime:
    print("primo")
else:
    print("não primo")


