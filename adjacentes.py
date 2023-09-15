numero = int(input("Digite o valor de n: "))

adjacente = 0

while numero != 0:
    pares = numero % 100
  #  print("pares = ", pares)

    algarismo1 = pares % 10
    algarismo2 = pares // 10

    if algarismo1 == algarismo2:
        adjacente = adjacente + 1

 #   print("algarismo1 = ", algarismo1)
 #   print("algarismo2 = ", algarismo2)

    numero = numero // 10


if adjacente > 0:
    print("sim")
else:
    print("não")



