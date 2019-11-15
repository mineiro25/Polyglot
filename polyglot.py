#!/usr/bin/python3

import argparse
import re
from difflib import get_close_matches
from langdetect import detect, detect_langs 

def isNotEmpty(lista):
    if lista != []:
        return True
    else:
        return False

def ptCalc(ficheiro):
    ficheiro = ficheiro.read()
    
    valorPt = 0

    """ 
        Identificação da lingua portuguesa

    """
    #Verifica se algum caracter esta em alguma das listas abaixo
    acentosPT = re.findall(r'[àèìòù]|[áéíóú]|[âêîôû]|[ãõ]|[ÀÈÌÒÙ]|[ÁÉÍÓÚ]|[ÂÊÎÔÛ]|[ÃÕ]', ficheiro)
    valorPt += 100 if isNotEmpty(acentosPT) else 0

    #Verifica a existencia de palavras que contenham hifens
    hifenPT = re.findall(r'([A-Za-z]-[a-z])', ficheiro)
    valorPt += 100 if isNotEmpty(hifenPT) else 0

    #Verifica se o texto tem alguma destas palavras (auxilio para detecao da lingua)
    palavrasPT = re.findall(r'\sda\s|\sde\s|\sdi\s|\sdo\s|\sdu\s|\sque\s|\sem\s|\scomo\s|\sos\s|\sas\s|\s[a-z]\s', ficheiro)
    valorPt += 100 if isNotEmpty(palavrasPT) else 0

    #Numeros
    numerosPT = re.findall(r'\sum\s|\sdois\s|\strês\s|\squatro\s|\scinco\s|\sseis\s|\ssete\s|\ssoito\s|\snove\s|\sdez\s',ficheiro)
    valorPt += 100 if isNotEmpty(numerosPT) else 0

    return valorPt

def esCalc(ficheiro):
    ficheiro = ficheiro.read()

    valorES = 0

    """ 
        Identificação da lingua espanhola

    """
    #Verifica se algum caracter esta em alguma das listas abaixo
    acentosES = re.findall(r'[àèìòù]|[áéíóú]|[âêîôû]|[ãõ]|[ÀÈÌÒÙ]|[ÁÉÍÓÚ]|[ÂÊÎÔÛ]|[ÃÕ]|[ñÑ]', ficheiro)
    valorES += 10 if isNotEmpty(acentosES) else 0

    #Verifica se alguam frase incia-se com estas pontuação
    pontuacaoES = re.findall(r'[¡!¿?]', ficheiro)
    valorES += 10 if isNotEmpty(pontuacaoES) else 0

    #Verifica se o texto tem alguma destas palavras (auxilio para detecao da lingua)
    palavrasES = re.findall(r'\ses\s|\suna\s|\sy\s|\suno\s|\sda\s|\sde\s|\sdi\s|\sdo\s|\sdu\s|\sla\s|\sle\s|\sli\s|\slo\s|\slu\s', ficheiro)
    valorES += 10 if isNotEmpty(palavrasES) else 0

    #Numeros
    numerosES = re.findall(r'\suno\s|\sdos\s|\stres\s|\scuatro\s|\scinco\s|\sseis\s|\ssiete\s|\socho\s|\snueve\s|\sdiez\s',ficheiro)
    valorES += 10 if isNotEmpty(numerosES) else 0

    return valorES

def engCalc(ficheiro):
    ficheiro = ficheiro.read()

    valorEng = 0

    """ 
        Identificação da lingua inglesa

    """
    #Verifica a existencia de palavras que contenham hifens
    plicasENG = re.findall(r'([A-Za-z]’[a-z])', ficheiro)
    valorEng += 1 if isNotEmpty(plicasENG) else 0

    #Verifica se o texto tem alguma destas palavras (auxilio para detecao da lingua)
    palavrasENG = re.findall(r'\ssaid\s|\slike\s|\sthis\s|\sthat\s|\swould\s|\shere\s|\swhere\s|\sdid\s|\sto\s|\sthe\s|\swas\s|\shis\s|\sher\s|\sit\s', ficheiro)
    valorEng += 1 if isNotEmpty(palavrasENG) else 0

    #Numeros
    numerosENG = re.findall(r'\sone\s|\stwo\s|\sthree\s|\sfour\s|\sfive\s|\ssix\s|\sseven\s|\seight\s|\snine\s|\sten\s',ficheiro)
    valorEng += 1 if isNotEmpty(numerosENG) else 0

    return valorEng

def getLanguage(ficheiro):

    valorPt = ptCalc(ficheiro)
    valorEs = esCalc(ficheiro)
    valorEng = engCalc(ficheiro)

    valores = {valorPt:"pt", valorEs:"es", valorEng:"en"}
    
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

    #Compares the iso code with the keys availabe in the dict_paises dictonary
    realLang = get_close_matches(valores.get(max(valores)), dict_paises)

    print(dict_paises[realLang[0]])

    #Returns the first result
    return dict_paises[realLang[0]]


def run(args):
    ficheiro = open(args.file, "r")

    getLanguage(ficheiro)





def main():
    parser = argparse.ArgumentParser(description="PALHA PALHA A DESCREVER O QUE ISTO FAZ!")
    parser.add_argument("-l", help="Retorna a lingua com o qual o texto foi escrito", dest="file", type=str)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()