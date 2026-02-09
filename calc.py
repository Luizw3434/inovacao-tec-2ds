# Etapa 1: Solicitar os 4 números via input
# O usuário vai fornecer 4 números separados por espaço
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
numero3 = input("Digite o terceiro número: ")
numero4 = input("Digite o quarto número: ")

# Etapa 2: Converter os valores para float
# Precisamos converter as entradas do usuário, que são do tipo string, para números de ponto flutuante (float)
numero1 = float(numero1)
numero2 = float(numero2)
numero3 = float(numero3)
numero4 = float(numero4)

# Etapa 3: Calcular a média
# A média é calculada somando os números e dividindo o total por 4
media = (numero1 + numero2 + numero3 + numero4) / 4

# Etapa 4: Exibir o resultado com duas casas decimais
# Usamos a função 'print' para exibir a média com duas casas decimais usando formatação
print(f"A média dos números é: {media:.2f}")
