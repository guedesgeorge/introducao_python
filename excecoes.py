print("Captura de excções")
 
try:
    numero = int(input("Digite um exemplo"))
    resultadp = 10 / numero
    print(f"resultado: {resultado}")
except Exception as e:
    print(f"Erro: {e}")