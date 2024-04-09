# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Entrada de dados
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em m): "))

# Calculando o IMC
imc = calcular_imc(peso, altura)

# Exibindo o resultado
print(f"O seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25.0 <= imc < 29.9:
    print("Sobrepeso")
elif 30.0 <= imc < 34.9:
    print("Obesidade grau I")
elif 35.0 <= imc < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III (mórbida)")