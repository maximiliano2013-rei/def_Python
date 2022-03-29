def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

a, b = 4,5
resultado = (subtrair if a > b else somar)(a, b)

print(f"Resultado: {resultado}")