def saudacao(nome):
  print(f"Ola, {nome}!")


# o codigo se houver espaçamento nao sera lido pelo compilador
print("\n chamando a funcão saudacao: ")
saudacao("Alice")
saudacao("Bob")



# função com retorno 

def quadrdo (numero):
  resultado = numero ** 3
  return resultado

print("\n chamando funcao quadrado:")
resultado_quadrado = quadrdo(5)
print("Resultado quadrado", resultado_quadrado)




def soma(numero1, numero2):
  resultado = numero1 + numero2 
  return resultado

print("Chamando a função soma")
resultado_soma = soma(20, 50)
print("A soma do numero 20 e numero 50 eh", resultado_soma)