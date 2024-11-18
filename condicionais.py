idade = int(input("quantos anos voce tem "))

if idade >= 18:
    print("Você é maior de idade")
elif idade >= 12:
    print("Você é um adolescente")
else:
    print("Você é menor de idade")

# Esta linha será executada independente da condição acima
mensagem = "Pode tirar carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)


## 

# Loop com for
numeros = [10, 20, 30]
for numero in numeros:
    print(f"Número: {numero}")

# Loop com while
contador = 0
while contador < len(numeros):
    print(f"Contador: {numeros[contador]}")
    contador += 1
