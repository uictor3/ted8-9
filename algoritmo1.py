vetor = []

for i in range(20):
 numeros = int(input(f"Digite o {i+1} número: "))
vetor.append(numeros)

print("Números na ordem inversa:")
for i in range(19, -1, -1):
 print(vetor[i])