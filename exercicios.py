# #### Inteiros (`int`)
import math
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
soma = num_int1 + num_int2
print(f"A soma de {num_int1} e {num_int2} é: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
int_num = int(input("Digite um número inteiro: "))
resto_divisao = int_num % 5
print(f"O resto da divisão de {int_num} por 5 é: {resto_divisao}")


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
produto = num1 * num2
print(f"O produto de {num1} e {num2} é: {produto}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

resultado = numero1 // numero2

print(f"A divisão inteira de {numero1} por {numero2} é: {resultado}")
print(resultado)
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero0 = int(input("Digite um número inteiro: "))
numero0_ao_quadrado = numero0 ** 2
print(f"O quadrado de {numero0} é: {numero0_ao_quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
float_num1 = float(input("Digite o primeiro número flutuante: "))
float_num2 = float(input("Digite o segundo número flutuante: "))
soma_float = float_num1 + float_num2
print(f"A soma de {float_num1} e {float_num2} é: {soma_float}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero4 = float(input("Digite o primeiro número flutuante: "))
numero5 = float(input("Digite o segundo número flutuante: "))
numeros_flutuantes = [numero4, numero5]
media = sum(numeros_flutuantes) / len(numeros_flutuantes)
# print(f"A média é: {media}")
# OR
# media = (numero4 + numero5) / 2

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numero_base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = numero_base ** expoente
print(f"{numero_base} elevado a {expoente} é: {potencia}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
# calculo matematico para converter Celsius para Fahrenheit = (C * 9/5) + 32 (or C * 1.8 + 32)
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("digite o raio:"))
# square = **2 = ao quadrado
area_do_circulo = math.pi * (raio_do_circulo ** 2)
# formação de string para limitar a quantidade de casas decimais a 2, usando :.2f
print(f"A área do círculo com raio {raio_do_circulo} é: {area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
str_usuario = input("Digite uma string: ")
# método .upper() para converter a string para maiúsculas
str_maiuscula = str_usuario.upper()
print(f"A string em maiúsculas é: {str_maiuscula}")


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")
# método .lower() para converter a string para minúsculas
nome_minusculo = nome_completo.lower()
print(f"Seu nome em minúsculas é: {nome_minusculo}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
escreva_frase = input("Digite uma frase: ")
# método .strip() para remover os espaços em branco no início e no final da string
frase_sem_espacos = escreva_frase.strip()
print(
    f"A frase sem espaços em branco no início e no final é: '{frase_sem_espacos}'")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
data_separada = data.split("/")
print(data_separada)  # Exibe a lista resultante da separação da string
dia = data_separada[0]
mes = data_separada[1]
ano = data_separada[2]
print(f"Dia: {dia}")    # Exibe o dia extraído da data
print(f"Mês: {mes}")   # Exibe o mês extraído da data
print(f"Ano: {ano}")  # Exibe o ano extraído da data

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
print(f"A concatenação das strings é: {string1 + ',' + string2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = input("Digite a primeira expressão booleana (True/False): ")
expressao2 = input("Digite a segunda expressão booleana (True/False): ")
avaliacao_and = (expressao1 == "") and (expressao2 == "")
print(f"O resultado da operação AND entre as expressões é: {avaliacao_and}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor8 = input("Digite o primeiro valor booleano (True/False): ")
valor9 = input("Digite o segundo valor booleano (True/False): ")
resulyado_OR = valor8 or valor9
print(f"O resultado da operação OR entre os valores é: {resulyado_OR}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
bool1 = input("Digite um valor booleano (True/False): ")
if bool1 == "True" or 0:
    bool_invertido = False
elif bool1 == "False" or 0:
    bool_invertido = True
else:  # bool1 == "" condição errada para o script
    bool_invertido = "Valor inválido. Por favor, insira 'True' ou 'False'."
print(f"O valor booleano invertido é: {bool_invertido}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero7 = int(input("Digite o primeiro número inteiro: "))
numero8 = int(input("Digite o segundo número inteiro: "))
if numero7 == numero8:
    valores_iguais = True
else:
    valores_iguais = False
# elif numero7 != numero8: # condição errada para o script
#    valores_iguais = "Valor inválido. Por favor, insira outros números."
print(f"Os números {numero7} e {numero8} são iguais? {valores_iguais}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
numero9 = int(input("Digite o primeiro número inteiro: "))
numero10 = int(input("Digite o segundo número inteiro: "))
if numero9 != numero10:
    valores_diferentes = True
else:
    valores_diferentes = False
print(
    f"Os números {numero9} e {numero10} são diferentes? {valores_diferentes}")

# #### try-except e if

# 21: Conversor de Temperatura
temperatura_geral = float(input("Digite a temperatura(apenas o número): "))
graus = input(
    "Digite a unidade de temperatura (C para Celsius, F para Fahrenheit): ")
if graus == "C":
    fahrenheit = (temperatura_geral * 9/5) + 32
    print(f"{temperatura_geral}°C é igual a {fahrenheit}°F")
elif graus == "F":
    celsius = (temperatura_geral - 32) * 5/9
    print(f"{temperatura_geral}°F é igual a {celsius}°C")
else:
    print("Unidade de temperatura inválida. Por favor, insira 'C' para Celsius ou 'F' para Fahrenheit.")


# 22: Verificador de Palíndromo
entrada_palindromo = input("Digite uma palavra ou frase: ")
# Remove espaços e converte para minúsculas para verificar o palíndromo
entrada_verificada = entrada_palindromo.replace(" ", "").lower()
# Verifica se a string é igual à sua inversa
if entrada_verificada == entrada_verificada[::-1]:
    print(f"'{entrada_palindromo}' é um palíndromo.")
else:
    print(f"'{entrada_palindromo}' não é um palíndromo.")

# 23: Calculadora Simples
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado de {numero1} + {numero2} é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado de {numero1} - {numero2} é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado de {numero1} * {numero2} é: {resultado}")
elif operacao == "/":
    resultado = numero1 / numero2
    print(f"O resultado de {numero1} / {numero2} é: {resultado}")
else:
    print("Operação inválida. Por favor, insira uma operação válida (+, -, *, /).")


# adicao = float(input("Digite o primeiro número para adição: "))
# subtracao = float(input("Digite o segundo número para subtração: "))
# multiplicacao = float(input("Digite o terceiro número para multiplicação: "))
# divisao = float(input("Digite o quarto número para divisão: "))


# 24: Classificador de Números
tipo_numero = float(input("Digite um número: "))
try:
    tipo_numero = float(tipo_numero)
except ValueError:
    print("Valor inválido. Por favor, insira um número válido.")
if tipo_numero > 0:
    print(f"O número {tipo_numero} é positivo.")
elif tipo_numero < 0:
    print(f"O número {tipo_numero} é negativo.")
elif tipo_numero == 0:
    print(f"O número {tipo_numero} é zero.")
par = tipo_numero % 2 == 0
impar = tipo_numero % 2 != 0

if par:
    print(f"O número {tipo_numero} é par.")
elif impar:
    print(f"O número {tipo_numero} é ímpar.")

# 25: Conversão de Tipo com Validação
lista_numeros_usuario = input(
    "Digite uma lista de números separados por vírgula: ")
try:
    numeros_str = lista_numeros_usuario.split(",")
    lista_inteiros = []

    for num in numeros_str:
        valor = float(num.strip())
        if not valor.is_integer():
            raise ValueError("Número não é inteiro")
        lista_inteiros.append(int(valor))

    print(f"Lista de números convertida: {lista_inteiros}")
except ValueError:
    print("Valor inválido. Por favor, insira apenas números inteiros separados por vírgula.")

# OR

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")
