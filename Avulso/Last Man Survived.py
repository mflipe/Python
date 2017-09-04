
# Casos de teste
# 1 <= T <= 20
T = 3
# 0 <= Ni <= 500
N1 = 7      # 7 Pessoas
N2 = 100    # 100 Pessoas
N3 = 245    # 245 Pessoas

# Saida Esperada
# 7
# 73
# 235

# Variaveis auxiliares
arma = 0

n1 = [x for x in range(1, N1+1)]

print(n1) # deBug

if len(n1)%2 == 0:
    mortos = len(n1)/2
else:
    mortos = round(len(n1)/2)-1


while arma <= len(n1):
    if len(n1) == 1:
        break
    print('Lista = ', n1)
    print('Arma = ', arma, ' --> Morre o', n1[arma+1])
    del n1[arma+1]
    #print(len(n1))
    if arma <= len(n1)-mortos:
        arma += 1
    else:
        print('Lista = ', n1)
        arma = 0
        print('Arma = ', arma, ' --> Morre o', n1[0])
        del n1[0]
        arma = 0

print('Lista = ', n1) # deBug
print('[FIM]')
