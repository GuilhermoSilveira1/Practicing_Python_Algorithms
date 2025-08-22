# Lista de Nomes
# Peça ao usuário 5 nomes e armazene numa lista. Depois mostre em ordem alfabética.

# Contagem de Palavras
# Receba uma frase e mostre quantas palavras diferentes ela tem (usar split e set).

# Fatorial
# Receba um número e calcule o fatorial dele.

# Sequência de Fibonacci
# Mostre os n primeiros números da sequência.

# Caixa Eletrônico Simples
# Peça um valor e simule a retirada do dinheiro mostrando quantas notas de cada valor seriam entregues (100, 50, 20, 10, 5, 2, 1).
def caixa(num):
    notas_100 = num % 100 
    resto = num / 100
    notas_50 = resto % 50
    resto = resto /50
    notas_20 = resto % 20
    resto = resto /20
    notas_10 = resto % 10
    resto = resto /10
    notas_5 = resto % 5
    resto = resto / 5
    notas_2 = resto % 2
    resto = resto / 2
    notas_1 = resto

    print(f'O valor R${num} será entregue em {notas_100} notas de 100, {notas_50} notas de 50, {notas_20}, notas de 20, {notas_10} notas de 10, {notas_5} notas de 5, {notas_2} notas de 2, {notas_1} notas de 1.')