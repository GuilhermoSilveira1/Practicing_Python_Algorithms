# Maior de Três Números
# Receba três números e exiba qual é o maior.
def maior_num(num1, num2, num3):
    print(f'O maior número entre {num1}, {num2}, {num3} é: {max(num1,num2,num3)}')

# Calculadora Simples
# Receba dois números e uma operação (+, -, *, /) e exiba o resultado.
def calculadora(num1, num2, operacao):
    match operacao:
        case 'soma':
            resultado = num1 + num2
        case 'subtracao':
            resultado = num1 + num2
        case 'multiplicacao':
            resultado = num1 * num2
        case 'divisao':
            resultado = num1 / num2
    print(f'O resultado da operação {operacao} é: {resultado}')

# Contador de Vogais
# Receba uma palavra/frase e mostre quantas vogais existem nela.
def contador_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    print(f'A quantidade de vogais no texto {texto} é: {contador}')

# Palíndromo
# Verifique se uma palavra é igual quando lida de trás para frente (ex: "arara", "radar").
def palindromo(palavra):
    if  palavra == palavra[::-1]:
        print(f'A palavra {palavra} é um palíndromo')
    else:
        print(f'A palavra {palavra} não é um palíndromo')

# Números Pares
# Mostre todos os números pares de 1 até um número informado.
def num_par(num):
    numeros_pares = []
    for i in range(1, num):
        if i % 2 == 0:
            numeros_pares.append(i)
    print(f'Os números entre {i} e {num} que são pares são: {numeros_pares}')