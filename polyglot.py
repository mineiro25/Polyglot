#!/usr/bin/python3

import argparse
import re
from difflib import get_close_matches
from translate import Translator
import os
import time
import playsound
import speech_recognition as speech_rec 
from gtts import gTTS

#Variavel global que contara todas as ocorrencias de linguas
totalOcurrencias =0
#Lingua origem
oLang = "English"
#Lingua destino
destLang = "Portuguese"

def speak(ficheiro):
    ficheiro = ficheiro.read()
    #Vai criar um objeto gTTS, com conteudo "ficheiro" e com a especificação da linguagem do texto
    texto = gTTS(text=ficheiro , lang='pt')
    nomeFich = str("textoPT" + ".mp3")
    #Cria e guarda um ficheiro de formato .mp3 para posteriormente ser reproduzido
    texto.save(nomeFich)
    playsound.playsound(nomeFich)

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

    #Pronomes
    pronomesPT = re.findall(r'\smeu\s|\sminha\s|\smeus\s|\sminhas\s|\snosso\s|\snossa\s|\snossos\s|\snossas\s|\steu\s|\stua\s|\steus\s|\stuas\s|\svosso\s|\svossa\s|\svossos\s|\svossas\s|\sseu\s|\ssua\s|\sseus\s|\ssuas\s|\sseu\s|\ssua\s|\sseus\s|\ssuas\s|\scujo\s|\scuja\s|\scujos\s|\scujas\s|\squanto\s|\squanta\s|\squantos\s|\squantas\s|\squal\s|\squais\s|\squem\s|\smuito\s|\spouco\s|\stanto\s|\stodo\s|\snenhum\s|\salgum\s|\scerto\s|\soutro\s|\squalquer\s|\smuita\s|\spouca\s|\stanta\s|\stoda\s|\snenhuma\s|\salguma\s|\scerta\s|\soutra\s|\squalquer\s|\smuitos\s|\spoucos\s|\stantos\s|\stodos\s|\suns\s|\snenhuns\s|\salguns\s|\scertos\s|\soutros\s|\squaisquer\s|\sambos\s|\smuitas\s|\spoucas\s|\stantas\s|\stodas\s|\sumas\s|\snenhumas\s|\salgumas\s|\scertas\s|\soutras\s|\squaisquer\s|\sambas\s|\salguém\s|\scada\s|\studo\s|\sninguém\s|\snada\s|\squal\s|\soutrem\s',ficheiro)
    valorPt += len(pronomesPT)
    totalOcurrencias += len(pronomesPT)    

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

    #Pronomes
    pronomesES = re.findall(r'\syo\s|\snosotros\s|\snosotras\s|\stú\s|\susted\s|\svosotros\s|\svosotras\s|\sustedes\s|\sél\s|\sella\s|\sello\s|\sellos\s|\sellas\s|\sme\s|\snos\s|\ste\s|\sos\s|\slo\s|\sla\s|\slos\s|\slas\s|\sles\s|\seste\s|\sese\s|\saquel\s|\sestos\s|\sesos\s|\saquellos\s|\sesta\s|\sesa\s|\saquella\s|\sestas\s|\sesas\s|\saquellas\s|\seso\s|\sesto\s|\saquello\s|\smi\s|\stu\s|\ssu\s|\snuestro\s|\svuestro\s|\snuestra\s|\svuestra\s|\smis\s|\stus\s|\ssus\s|\snuestros\s|\svuestros\s|\snuestras\s|\svuestras\s|\smío\s|\stuyo\s|\ssuyo\s|\smíos\s|\stuyos\s|\ssuyos\s|\smía\s|\stuya\s|\ssuya\s|\smías\s|\stuyas\s|\ssuyas\s|\slo mío\s|\slo tuyo\s|\slo suyo\s|\slo nuestro\s|\slo vuestro\s|\salgún\s|\salguno\s|\sningún\s|\sninguno\s|\scualquier\s|\soutro\s|\spoco\s|\smucho\s|\salgunos\s|\sotros\s|\spocos\s|\smuchos\s|\svários\s|\salguna\s|\sninguna\s|\scualquiera\s|\sotra\s|\spoca\s|\smucha\s|\squienquiera\s|\salgunas\s|\soutras\s|\spocas\s|\smuchas\s|\svarias\s',ficheiro)
    valorES += len(pronomesES)
    totalOcurrencias += len(pronomesES)   

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
    
    #Pronomes
    pronomesENG = re.findall(r'\sMe\s|\sYou\s|\sHim\s|\sHer\s|\sIt\s|\sUs\s|\sYou\s|\sThem\s|\sMy\s|\sYour\s|\sHis\s|\sHer\s|\sIts\s|\sOur\s|\sYour\s|\sTheir\s|\sMine\s|\sYours\s|\sHis\s|\sHers\s|\sIts\s|\sOurs\s|\sYours\s|\sTheirs\s|\sSomebody\s|\sAnybody\s|\sSomeone\s|\sAnyone\s|\sSomething\s|\sAnything\s|\sSomewhere\s|\sAnywhere\s|\sNobody\s|\sEverybody\s|\sNo one\s|\sEveryone\s|\sNothing\s|\sEverything\s|\sNowhere\s|\sEverywhere\s|\sme\s|\syou\s|\shim\s|\sher\s|\sit\s|\sus\s|\syou\s|\sthem\s|\smy\s|\syour\s|\shis\s|\sher\s|\sits\s|\sour\s|\syour\s|\stheir\s|\smine\s|\syours\s|\shis\s|\shers\s|\sits\s|\sours\s|\syours\s|\stheirs\s|\ssomebody\s|\sanybody\s|\ssomeone\s|\sanyone\s|\ssomething\s|\sanything\s|\ssomewhere\s|\sanywhere\s|\snobody\s|\severybody\s|\sno one\s|\severyone\s|\snothing\s|\severything\s|\snowhere\s|\severywhere\s',ficheiro)
    valorEng += len(pronomesENG)
    totalOcurrencias += len(pronomesENG)   

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

def dictCodePage():
    dict_codepage = {
        'Arabic' : 'cp1256',
        'Bulgarian' : 'cp1251',
        'Catalan' : 'cp1252',
        'Czech' : 'cp1250',
        'German' : 'cp1250',
        'Greek' : 'cp1253',
        'English' : 'cp1252',
        'Finnish' : 'cp1257',
        'French' : 'cp1252',
        'Galician' : 'cp1252',
        'Croatian' : 'cp1250',
        'Hungarian' : 'cp1250',
        'Italian' : 'cp1252',
        'Korean' : 'cp1363',
        'Latvian' : 'cp1257',
        'Lithuanian' : 'cp1257',
        'Macedonian' : 'cp1251',
        'Dutch' : 'cp1252',
        'Polish' : 'cp1257',
        'Portuguese' : 'cp1252',
        'Russian' : 'cp1251',
        'Swedish' : 'cp1252',
        'Slovak' : 'cp1250',
        'Slovenian' : 'cp1250',
        'Spanish' : 'cp1252',
        'Turkish' : 'cp1254',
        'Vietnamese' : 'cp1258'
    }

    return dict_codepage

def getLanguage(ficheiro):
    ficheiro.seek(0)

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
    print("Trust in the output:")
    for key, value in sorted(valores.items(), reverse=True) :
        print(key, value)

    #Returns the first result
    return dict_paises[realLang[0]]

def translator(ficheiroO, ficheiroD):

    global oLang
    global destLang

    #Dicionario com todos os paises
    dict_paises = dictPaises()
    #Dicionario com os codepages de diversos paises
    dict_codepage = dictCodePage()

    #Lingua do ficheiro recebido
    oLang = getLanguage(ficheiroO)

    #Recebe a lingua para o qual quer traduzir
    linguaDest = input("Por favor indique para lingua quer traduzir!\n")

    #Definir por default uma lingua
    tradutor = Translator(from_lang= oLang, to_lang= destLang)

    try:
        #Vai iterar pelo dicionario a procura da lingua mais proxima
        for chave, lingua in dict_paises.items():
            if linguaDest == lingua:
                destLang = linguaDest
        tradutor = Translator(from_lang= oLang, to_lang= destLang)
    except:
        print("Algo correu mal nas definições de linguagem!")
    
    #Compara as chaves do dicionario, com a lingua pretendida
    codepage = get_close_matches(destLang, dict_codepage.keys())

    ficheiroO.seek(0) #Garante que o ficheiro vai a ser lido do inicio
    #Escrita da traducao num texto
    output = open(ficheiroD, "w")
    linhas = re.split(r'(?s)((?:[^\n][\n]?)+)',ficheiroO.read())
    #Faz uma leitura por todos os elementos da lista, e remove todos os que sejam iguais a ''
    linhas = list(filter(lambda a: a != '', linhas))
    for linha in linhas:
        #Texto ja traduzido
        traducao = tradutor.translate(linha.encode(dict_codepage[codepage[0]]).decode())
        output.write(traducao + "\n")
    
    output.close()

    return traducao         

def clearText(ficheiro):
    ficheiro = ficheiro.read()

    #Limpa o ficheiro de acentos
    ficheiro = re.sub(r'[âãáà]','a',ficheiro)
    ficheiro = re.sub(r'[êéè]','e',ficheiro)
    ficheiro = re.sub(r'[îíì]','i',ficheiro)
    ficheiro = re.sub(r'[õôóò]','o',ficheiro)
    ficheiro = re.sub(r'[ûúù]','u',ficheiro)
    ficheiro = re.sub(r'[ÂÃÁÀ]','A',ficheiro)
    ficheiro = re.sub(r'[ÊÉÈ]','E',ficheiro)
    ficheiro = re.sub(r'[ÎÍÌ]','I',ficheiro)
    ficheiro = re.sub(r'[ÕÔÓÒ]','O',ficheiro)
    ficheiro = re.sub(r'[ÛÚÙ]','U',ficheiro)
    ficheiro = re.sub(r'ñ','n',ficheiro)
    ficheiro = re.sub(r'Ñ','N',ficheiro)

    return ficheiro

def isTranslation(ficheiroO, ficheiroD):
    #Criação de um ficheiro auxiliar para a verificação da tradução
    translator(ficheiroO, "Teste.txt")
    ficheiroO = open("Teste.txt", "r")
  
    #Pega em todas as palavras que comecem por maiusculas
    tokensO = re.findall(r'[A-Z][^ ]*', ficheiroO.read())
    tokensD = re.findall(r'[A-Z][^ ]*', ficheiroD.read())
    
    #Faz uma leitura por todos os elementos da lista, e remove todos os que sejam iguais a ''
    tokensO = list(filter(lambda a: a != '', tokensO))
    tokensD = list(filter(lambda a: a != '', tokensD))

    #Contador de tokens para depois indicar a confiança
    numTokensTot = 0
    numTokensTot += len(tokensO) + len(tokensD)

    #Contador tokens equivalentes
    numTokens = 0   

    #Verificação das palavras e suas supostas traduções
    for origem in tokensO:
        for destino in tokensD:
            if(origem == destino):
                numTokens += 1

    #Calculo da confiança
    confianca = numTokens/numTokensTot

    if(confianca == 0):
        print("Não é tradução!\nConfiança: " + str(confianca))
    elif(confianca > 0 and confianca <= 0.5):
        print("Poderá não ser tradução!\nConfiança: " + str(confianca))
    elif(confianca > 0.5 and confianca <= 0.65):
        print("Poderá ser tradução!\nConfiança: " + str(confianca))
    else:
        print("É tradução!\nConfiança: " + str(confianca))   
    
def run(args):
    if args.lang != None:
        ficheiro = open(args.lang, "r")
        getLanguage(ficheiro)
        ficheiro.close()
    elif args.translate != None:
        ficheiroO,ficheiroD = args.translate.split()
        ficheiroO = open(ficheiroO, "r")
        ficheiroD = open(ficheiroD, "r")
        translator(ficheiroO,ficheiroD)
        ficheiroO.close()
        ficheiroD.close()
    elif args.speech != None:
        ficheiro = open(args.speech, "r")
        speak(ficheiro)
        ficheiro.close()
    elif args.files != None:
        ficheiroO,ficheiroD = args.files.split()
        ficheiroO = open(ficheiroO, "r")
        ficheiroD = open(ficheiroD, "r")
        isTranslation(ficheiroO,ficheiroD)
        ficheiroO.close()
        ficheiroD.close()
    
def main():
    parser = argparse.ArgumentParser(description="PALHA PALHA A DESCREVER O QUE ISTO FAZ!")
    parser.add_argument("-l", help="Retorna a lingua com o qual o texto foi escrito", dest="lang", type=str, required= False)
    parser.add_argument("-t", help="Traduz um texto para a lingua pretendida", dest="translate", type=str, required= False)
    parser.add_argument("-s", help="Lê o ficheiro indicado.", dest="speech", type=str, required=False)
    parser.add_argument("-c", help="Verifica se um ficheiro é tradução do outro", dest="files", type=str, required=False)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()