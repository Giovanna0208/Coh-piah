import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relacao Type-Token:"))
    hlr = float(input("Entre a Razao Hapax Legomana:"))
    sal = float(input("Entre o tamanho medio de sentenca:"))
    sac = float(input("Entre a complexidade media da sentenca:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    
    valorLinguistico = 0
    
    for i in range(0,6):
        valor = as_a[i] - as_b[i]
        
        if (valor < 0): 
            valor *= -1
            
        valorLinguistico += valor
    
    return valorLinguistico / 6


def calcula_assinatura(texto):
    
    conjSentencas = separa_sentencas(texto)
    
    conjFrases = extrai_frases(conjSentencas)

    conjPalavras = extrai_palavras(conjFrases)
    
    wal = calcula_tamanho_medio_palavra(conjPalavras)
    ttr = calcula_typen_token(conjPalavras)
    hlr = calcula_Hapax_Legomana(conjPalavras)
    
    sal = calcula_tamanho_medio_sentencas(conjSentencas)
    sac = calcula_complexidade_sentenca(conjFrases, len(conjSentencas))
    pal = calcula_tamanho_medio_frase(conjFrases)
   
    return [wal, ttr, hlr, sal, sac, pal]
    
def avalia_textos(textos, ass_cp):
    
    assinaturas = []
    for te in textos:
        assinaturas.append(calcula_assinatura(te))

    grauSimilaridade = 1000.0
    numTex = -1
    
    for i in range( 0, len(assinaturas)):
        
        similaridade = compara_assinatura(ass_cp, assinaturas[i])
        
        if (similaridade < grauSimilaridade):
            grauSimilaridade = similaridade
            numTex = i + 1

    return numTex

def extrai_frases(sentencas):
    
    frases = []
    
    for sentenca in sentencas:
        
        frases += separa_frases(sentenca)
        
    return frases
    
def extrai_palavras(sentencas):
    
    palavras = []
    
    frases = extrai_frases(sentencas)
    
    for frase in frases:

        palavras += separa_palavras(frase)
    
    return palavras
    
def calcula_tamanho_medio_palavra(palavras):
    
    tamanho = 0
    
    for pal in palavras:
        tamanho += len(pal)
    
    return tamanho / len(palavras)

def calcula_typen_token(palavras):
    
    numPalavrasDif = n_palavras_diferentes(palavras)
    
    return numPalavrasDif / len(palavras)
    
def calcula_Hapax_Legomana(palavras):

    numPalavasUnicas = n_palavras_unicas(palavras)
    
    return numPalavasUnicas / len(palavras)
    
def calcula_tamanho_medio_sentencas(sentencas):
    # delimitadores: .!?
    
    tamanho = 0
    
    for sentenca in sentencas:
        s = re.sub(r'[.!?]+', "", sentenca)
        tamanho += len(s)
    
    return tamanho / len(sentencas)

def calcula_complexidade_sentenca(frases, numeroSentencas):
    
    numFrases = len(frases)

    return numFrases / numeroSentencas

def calcula_tamanho_medio_frase(frases):
    
    tamanho = 0
    
    for frase in frases:
        f =  re.sub(r'[,:;]+', "", frase)
        tamanho += len(f)
        
    return tamanho / len(frases)

def main():

    assinaturaPadrao = le_assinatura()
    
    textos = le_textos()

    numSimilar = avalia_textos(textos, assinaturaPadrao)
    
    print("O autor do texto {} esta infectado com COH-PIAH".format(numSimilar))
    
main()
