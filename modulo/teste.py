print("Exemplo de criação e utilazação de um modulo personalizado")

import meu_modulo as meu_modulo

mensagem = meu_modulo.saudacao("george")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")