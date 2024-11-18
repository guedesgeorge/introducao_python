# criando um dicionario de exemplo
pessoa = {"nome": "George", "idade": 21, "cidade": "São Paulo" }

print("Meu dicionario de exemplo", pessoa)

# acessando valores por chave 

print("nome", pessoa["nome"])
print("idade", pessoa["idade"])
print("cidade", pessoa["cidade"])

pessoa["sobrenome"] = "Guedes"
print("sobrenome", pessoa["sobrenome"])

# mudando valores da chave
pessoa["idade"] = 22
print("idade:", pessoa["idade"])

# Reomovendo um par chave-valor

del pessoa["sobrenome"]
print("Meu dicionario exemplo", pessoa)

# metodo keys serve para acessar e ver quantas chaves-valor tem 
chaves = list(pessoa.keys()) 
print("Chaves do dicionario: ", chaves)

# para acessar uma chave especifica 
print("Primeira chave", chaves[0])


# metodos values 

valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor do dicionario ", valores[1])

# metodos itens 
itens = list(pessoa.items())
print("Primeiro valor:", itens[0][1])