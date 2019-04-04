import math


# Esquece essa porra
def multiplicar(num, peso):
    for x in range(len(num)):
        num[x] *= peso[x]
    return num


# Declaração do modelo do perceptron
def perc(num, peso, bias):
    return 1/(1+(math.exp(-(sum(multiplicar(num, peso), bias)))))
    

# Código aqui
f = open("semeion.data", "r")
backup = f.readline().split(" ")
print(backup)
for z in range(256):
    matriz = [[int(float(backup[z])) for x in range(16)] for y in range(16)]
for x in range(16):
    print(matriz[x])
f.close()
exit(1)


