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
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("digite o raio:"))
# square = **2 = ao quadrado
area_do_circulo = math.pi * (raio_do_circulo ** 2)
# formação de string para limitar a quantidade de casas decimais a 2, usando :.2f
print(f"A área do círculo com raio {raio_do_circulo} é: {area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
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


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
