# Exercícios de Manipulação de Strings
# Contador de Caracteres
# Receba uma frase e conte quantos caracteres ela tem (sem contar espaços).
def contar_caracteres(texto):
    texto_sem_espacos = texto.replace(" ", "")
    print(f'A frase possui {len(texto_sem_espacos)} caracteres sem contar os espaços')

# Inversor de Texto
# Receba uma palavra ou frase e exiba ela invertida.
def inversor(frase):
    texto_invertido = frase[::-1]
    print(f'A frase/palavra {frase} invertida fica: {texto_invertido}')

# Remover Vogais
# Receba uma string e retorne ela sem vogais.
def sem_vogais(texto):
    vogais = 'aeiouAEIOU'
    texto_limpo = texto.replace(vogais, "")
    print(f'O texto {texto} sem vogais fica: {texto_limpo}')

# Substituir Palavras
# Receba uma frase e substitua uma palavra específica por outra.

# Verificador de Palíndromo
# Verifique se uma palavra ou frase é um palíndromo (mesmo texto ao contrário).
def palindromo(palavra):
    if palavra == palavra[::-1]:
        print(f'A palavra {palavra} é um palíndromo')
    else: 
        print(f'A palavra {palavra} não é um palíndromo')

# Contador de Letras
# Conte quantas vezes cada letra aparece em uma frase (dica: use dict ou collections.Counter).

# Formatação de Nome
# Receba um nome completo e retorne ele no formato: SOBRENOME, PrimeiroNome.
def ajustar_nome(nome):
    nome_sobrenome = nome.split
    sobrenome_nome = []
    sobrenome_nome[0].toUpper() = nome_sobrenome[1]
    sobrenome_nome[1] = nome_sobrenome[0]
    print(f'O nome ajustado fica: {sobrenome_nome}')

# Extrair Domínio de Email
# Receba um email e retorne apenas o domínio (ex: usuario@gmail.com → gmail.com).

# Remover Pontuação
# Receba uma frase e remova todos os sinais de pontuação.
def remover_sinais(frase):
    frase_limpa = frase.replace('!,.?', '')
    print(f'A frase sem pontuação fica: {frase_limpa}')

# Separar Palavras por Tamanho
# Receba uma frase e separe as palavras em duas listas: curtas (≤4 letras) e longas (>4 letras).
def listas(frase):
    palavras = frase.split()
    palavras_curtas = []
    palavras_longas = []
    for i in palavras:
        if len(palavras[i]) < 4 or len(palavras[i]) == 4:
            palavras_curtas.append(palavras[i])
        else:
            palavras_longas.append(palavras[i])