def maximo(x,y):
    if x>y:
        return x
    else:
        return y


def test_maximoWorks():
    assert maximo(4,2) == 4

def test_maximoWorks2():
    assert maximo(0,-1) == 0

