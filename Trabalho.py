import math
import numpy as np


# Esquece essa porra
def multiplicar(num, peso):
    for x in range(len(num)):
        num[x] *= peso[x]
    return num


# Declaração do modelo do perceptron
def perc(num, peso, bias):
    return 1/(1+(math.exp(-(sum(multiplicar(num, peso), bias)))))
    

# Abro o arquivo de imagem
f = open("semeion.data", "r")

list = f.readline().split(" ")

input = np.zeros(256)

#Converto os dados de lista para float
for x in range (256):
    input[x] = float(list[x])

#Declaro os pesos iniciais, por meio da função de He-et-al
whl = np.random.randn(16, 256) * np.sqrt(2 / 256)

wout = np.random.randn(10, 16) * np.sqrt(2 / 16)

#Declaro a hidden layer
hl = np.zeros(16)

output = np.zeros(10)

bias = 0

for x in range (16):
    hl[x] = perc(input, whl[x], bias)

for x in range (10):
    output[x] = perc(hl, wout[x], bias)
print(output)
print(max(output))


f.close()