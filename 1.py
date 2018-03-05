import numpy as np

def soma(lis1, lis2):
    somatorio = 0
    somatorio2 = 0
    for i in range(len(lis1)):
        somatorio = somatorio + lis1[i]
        print(somatorio)
    
    for j in range(len(lis2)):
        if lis2[j] not in lis1:
            somatorio2 = somatorio2 + lis2[j]
            print(somatorio2)
    return somatorio + somatorio2    
a = np.arange(3, 1000, 3)
b = np.arange(5, 1000, 5)

print(soma(a, b))