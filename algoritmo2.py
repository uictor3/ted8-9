numero = []
for i in range (0, 20):
    n = int(input('Digite um número:'))
    if i == 0 or n > numero[-1]:
        numero.append(n)
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero[pos]:
              numero.insert(pos, n)
            break
        pos += 1
print('-=' * 30)
print(f' Os números digitados em ordem foram {numero}')