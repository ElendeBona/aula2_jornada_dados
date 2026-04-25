# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")
if len(nome) == 0:
    raise ValueError("O nome não pode ser vazio.")
elif any(char.isdigit() for char in nome):
    # verifica se o nome contém números e lança um erro caso seja verdade
    raise ValueError("O nome não pode conter números.")
else:
    print(f"Olá, {nome}! Bem-vindo ao curso de Python para Dados!")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        raise ValueError("O salário não pode ser negativo.")
except ValueError:
    print("Erro: certifique-se de que o salário é um número válido e não negativo.")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus = float(input("Digite a porcentagem do bônus: "))
    if bonus < 0:
        raise ValueError("O bônus não pode ser negativo.")
except ValueError:
    print("Erro: certifique-se de que o bônus é um número válido e não negativo.")
# 4) Calcule o valor do bônus final

valor_do_bonus = 1000 + salario * bonus
kpi = valor_do_bonus + salario / 1000

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, o seu salário é R${salario:.2f} e o seu bônus foi de {valor_do_bonus:.2f}")
print(f"Seu KPI é: {kpi:.2f}")
