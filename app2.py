# arquivo: app.py

print("=== Sistema de Cadastro Simples ===")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome}, você é maior de idade.")
else:
    print(f"{nome}, você é menor de idade.")

print("Cadastro finalizado!")