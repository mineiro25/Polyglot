#!/usr/bin/python3


 https://www.youtube.com/watch?v=YapTts_An9A  

import argparse
import re
from difflib import get_close_matches
from translate import Translator

#Variavel global que contara todas as ocorrencias de linguas
totalOcurrencias =0

def ptCalc(ficheiro):
    ficheiro.seek(0) #Garante que o ficheiro vai a ser lido do inicio
    ficheiro = ficheiro.read()
    
    global totalOcurrencias
    valorPt = 0

    """ 
        Identificação da lingua portuguesa

    """
    #Verifica se algum caracter esta em alguma das listas abaixo
    acentosPT = re.findall(r'[àèìòù]|[áéíóú]|[âêîôû]|[ãõ]|[ÀÈÌÒÙ]|[ÁÉÍÓÚ]|[ÂÊÎÔÛ]|[ÃÕ]', ficheiro)
    valorPt += len(acentosPT)
    totalOcurrencias += len(acentosPT)

    #Verifica a existencia de palavras que contenham hifens
    hifenPT = re.findall(r'([A-Za-z]-[a-z])', ficheiro)
    valorPt += len(hifenPT)
    totalOcurrencias += len(hifenPT)

    #Verifica se o texto tem alguma destas palavras (auxilio para detecao da lingua)
    palavrasPT = re.findall(r'\sda\s|\sde\s|\sdi\s|\sdo\s|\sdu\s|\sque\s|\sem\s|\scomo\s|\sos\s|\sas\s|\suma\s', ficheiro)
    valorPt += len(palavrasPT)
    totalOcurrencias += len(palavrasPT)

    #Numeros
    numerosPT = re.findall(r'\sum\s|\sdois\s|\strês\s|\squatro\s|\scinco\s|\sseis\s|\ssete\s|\ssoito\s|\snove\s|\sdez\s',ficheiro)
    valorPt += len(numerosPT)
    totalOcurrencias += len(numerosPT)

    ficheiro.close()

    return valorPt

def esCalc(ficheiro):
    ficheiro.seek(0) #Garante que o ficheiro vai a ser lido do inicio
    ficheiro = ficheiro.read()
    
    global totalOcurrencias
    valorES = 0

    """ 
        Identificação da lingua espanhola

    """
    #Verifica se algum caracter esta em alguma das listas abaixo
    acentosES = re.findall(r'[àèìòù]|[áéíóú]|[âêîôû]|[ãõ]|[ÀÈÌÒÙ]|[ÁÉÍÓÚ]|[ÂÊÎÔÛ]|[ÃÕ]|[ñÑ]', ficheiro)
    valorES += len(acentosES)
    totalOcurrencias += len(acentosES)

    #Verifica se alguam frase incia-se com estas pontuação
    pontuacaoES = re.findall(r'[¡!¿?]', ficheiro)
    valorES += len(pontuacaoES)
    totalOcurrencias += len(pontuacaoES)

    #Verifica se o texto tem alguma destas palavras (auxilio para detecao da lingua)
    palavrasES = re.findall(r'\ses\s|\suna\s|\sy\s|\suno\s|\sda\s|\sde\s|\sdi\s|\sdo\s|\sdu\s|\sla\s|\sle\s|\sli\s|\slo\s|\slu\s', ficheiro)
    valorES += len(palavrasES)
    totalOcurrencias += len(palavrasES)

    #Numeros
    numerosES = re.findall(r'\suno\s|\sdos\s|\stres\s|\scuatro\s|\scinco\s|\sseis\s|\ssiete\s|\socho\s|\snueve\s|\sdiez\s',ficheiro)
    valorES += len(numerosES)
    totalOcurrencias += len(numerosES)

    ficheiro.close()

    return valorES

def engCalc(ficheiro):
    ficheiro.seek(0) #Garante que o ficheiro vai a ser lido do inicio
    ficheiro = ficheiro.read()
    
    global totalOcurrencias
    valorEng = 0

    """ 
        Identificação da lingua inglesa

    """
    #Verifica a existencia de palavras que contenham hifens
    plicasENG = re.findall(r'([A-Za-z]’[a-z])', ficheiro)
    valorEng += len(plicasENG)
    totalOcurrencias += len(plicasENG)

    #Verifica se o texto tem alguma destas palavras (auxilio para detecao da lingua)
    palavrasENG = re.findall(r'\ssaid\s|\slike\s|\sthis\s|\sthat\s|\swould\s|\shere\s|\swhere\s|\sdid\s|\sto\s|\sthe\s|\swas\s|\shis\s|\sher\s|\sit\s|\sour\s|\swith\s|\sreally\s|\sme\s|\sago\s|\sfor\s', ficheiro)
    valorEng += len(palavrasENG)
    totalOcurrencias += len(palavrasENG)

    #Numeros
    numerosENG = re.findall(r'\sone\s|\stwo\s|\sthree\s|\sfour\s|\sfive\s|\ssix\s|\sseven\s|\seight\s|\snine\s|\sten\s',ficheiro)
    valorEng += len(numerosENG)
    totalOcurrencias += len(numerosENG)

    ficheiro.close()
    
    return valorEng

def dictPaises():
    #Dicionario com todas as linguas
    dict_paises = {
        'ar' : 'Arabic',
        'bg' : 'Bulgarian',
        'ca' : 'Catalan',
        'cz' : 'Czech',
        'de' : 'German',
        'el' : 'Greek',
        'en' : 'English',
        'fa' : 'Persian (Farsi)',
        'fi' : 'Finnish',
        'fr' : 'French',
        'gl' : 'Galician',
        'hr' : 'Croatian',
        'hu' : 'Hungarian',
        'it' : 'Italian',
        'ja' : 'Japanese',
        'kr' : 'Korean',
        'la' : 'Latvian',
        'lt' : 'Lithuanian',
        'mk' : 'Macedonian',
        'nl' : 'Dutch',
        'pl' : 'Polish',
        'pt' : 'Portuguese',
        'ro' : 'Romanian',
        'ru' : 'Russian',
        'se' : 'Swedish',
        'sk' : 'Slovak',
        'sl' : 'Slovenian',
        'es' : 'Spanish',
        'tr' : 'Turkish',
        'ua' : 'Ukrainian',
        'vi' : 'Vietnamese',
        'zh_cn' : 'ChineseSimplified',
        'zh_tw' : 'ChineseTraditional'
    }

    return dict_paises

def getLanguage(ficheiro):

    global totalOcurrencias
    global realLang

    #Dicionario com todos os paises
    dict_paises = dictPaises()

    #Recebe todas as ocorrencias de cada lingua
    valorPt = ptCalc(ficheiro)
    valorEs = esCalc(ficheiro)
    valorEng = engCalc(ficheiro)

    #Saber a percentagem de ocurrências
    valorPt = valorPt/totalOcurrencias
    valorEs = valorEs/totalOcurrencias
    valorEng = valorEng/totalOcurrencias
    
    #Dicionario com todos os valores e respetivas chaves
    valores = {valorPt:"pt", valorEs:"es", valorEng:"en"}

    #Compares the iso code with the keys availabe in the dict_paises dictonary
    realLang = get_close_matches(valores.get(max(valores)), dict_paises)
    #retorno da lingua mais semelhante ao melhor resultado
    print("The text was written in: " + str(dict_paises[realLang[0]]))
    #Output das confiancas
    print("Trust in the output:\n")
    for key, value in valores.items() :
        print(key, value)

    #Returns the first result
    return dict_paises[realLang[0]]

def translator(ficheiro):
    ficheiro.seek(0) #Garante que o ficheiro vai a ser lido do inicio
    ficheiro = ficheiro.read()

    #Dicionario com todos os paises
    dict_paises = dictPaises()

    #Recebe a lingua para o qual quer traduzir
    linguaDest = input("Por favor indique para lingua quer traduzir!\n")

    #Definir por default uma lingua
    tradutor = Translator(to_lang = "en")

    #Vai iterar pelo dicionario a procura da lingua mais proxima
    for chave, lingua in dict_paises.items():
        if linguaDest == lingua:
            tradutor = Translator(to_lang = chave)

    
    #Escrita da traducao num texto
    output = open("Traducao.txt", "w")
    linhas = re.split(r'\n\n+',ficheiro)
    for linha in linhas:
        #Texto ja traduzido
        traducao = tradutor.translate(str(linha))
        output.write(traducao + "\n\n")
    
    output.close()

    return traducao         


def run(args):
    if args.lang != None:
        ficheiro = open(args.lang, "r")
        getLanguage(ficheiro)
    elif args.translate != None:
        ficheiro = open(args.translate, "r")
        translator(ficheiro)




def main():
    parser = argparse.ArgumentParser(description="PALHA PALHA A DESCREVER O QUE ISTO FAZ!")
    parser.add_argument("-l", help="Retorna a lingua com o qual o texto foi escrito", dest="lang", type=str, required= False)
    parser.add_argument("-t", help="Traduz um texto para a lingua pretendida", dest="translate", type=str, required= False)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()