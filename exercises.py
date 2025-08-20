# 🟢 Iniciante
# Esses exercícios ajudam a praticar sintaxe básica, estruturas de controle e tipos de dados simples.

# Par ou Ímpar: Receba um número e diga se ele é par ou ímpar.
def par_ou_impar(numero):
    if (numero % 2) == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é impar!')

par_ou_impar(6)

# Maior de Três: Receba três números e retorne o maior.
def maior(num1, num2, num3):
    if num1 > num2 & num3:
        resultado = num1
    elif num1 > num3:
        resultado = num2
    elif num2 > num1:
        resultado = num2
    elif num2 > num3:
        resultado = num2
    elif num3 > num1:
        resultado = num3
    elif num3 > num2:
        resultado = num3
    
    print(f'O maior número é {resultado}')

maior(3, 5, 10)

# Calculadora Simples: Implemente uma calculadora que realiza as quatro operações básicas.
def calculadora(num1, num2, operacao):
    match operacao:
        case 'soma':
            resultado = num1 + num2
        case 'subtração':
            resultado = num1 - num2
        case 'divisão':
            resultado = num1 / num2
        case 'multiplicação':
            resultado = num1 * num2

    print(f'O resultado da operação de {operacao} é: {resultado}')

calculadora(2, 3, 'soma')

# Contador de Vogais: Conte quantas vogais há em uma string.


# Fatorial: Calcule o fatorial de um número usando for ou while.
def fatorial(num):
    resultado = 1
    if num == 1:
        return resultado
    else:
        resultado = resultado * num
        num =- 1
        fatorial(num)

fatorial(3)

# 🟡 Intermediário
# Aqui você começa a usar listas, funções e manipulação de strings mais avançada.

# Ordenação Manual: Ordene uma lista de números sem usar sort().
# Palíndromo: Verifique se uma palavra ou frase é um palíndromo.
# Busca Linear: Implemente uma função que busca um valor em uma lista.
def busca(valor, lista):
    for valores in lista:
        if valor == valores:
            print(f'O valor {valor} está presente na lista!')
            return valores
        else:
            print(f'O valor {valor} não está presenta na lista.') 

# Conversor de Base: Converta um número decimal para binário.
# Contador de Palavras: Conte quantas vezes cada palavra aparece em um texto.
 

# 🔴 Avançado
# Esses envolvem algoritmos clássicos e estruturas como dicionários, conjuntos e recursão.

# Sequência de Fibonacci: Gere os primeiros N números da sequência.
# Anagramas: Verifique se duas palavras são anagramas.
# Jogo da Forca (texto): Implemente uma versão simples do jogo da forca.
# Validador de CPF: Crie um algoritmo que valide um CPF.
# Sudoku Checker: Verifique se uma matriz 9x9 representa uma solução válida de Sudoku.
