def ePrimo(number):
    i = 2
    isPrime = True
    while i < number:
        if number % i == 0:
            isPrime = False
        i = i + 1
    if isPrime:
        return True
    else:
        return False


def test_ePrimo():
    assert ePrimo(17) == True

def test_ePrimo2():
    assert ePrimo(40) == False

def maior_primo(numero):
    i = 0
    primoNumber = 0
    while(i <= numero):
        if(ePrimo(i) == True):
            primoNumber = i
        i = i + 1
    return primoNumber

def test_maiorPrimo():
    assert maior_primo(10) == 7

def test_maiorPrimo2():
    assert  maior_primo(100) == 97

def test_maiorPrimo3():
    assert maior_primo(7) == 7