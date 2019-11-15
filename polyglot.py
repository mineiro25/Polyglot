#! /usr/bin/env pyhton

import argparse
import re
from difflib import get_close_matches
from langdetect import detect, detect_langs 


def getLanguage(text):
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
        'ro' : 'Russian',
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

    #Return the iso code of the correspondent coutry
    lang = detect(text)

    #Compares the iso code with the keys availabe in the dict_paises dictonary
    realLang = get_close_matches(lang, dict_paises)

    #Returns the first result
    return dict_paises[realLang[0]]



def run(args):
    text = args.text

    getLanguage(text)





def main():
    parser = argparse.ArgumentParser(description="PALHA PALHA A DESCREVER O QUE ISTO FAZ!")
    parser.add_argument("-teste", help="Palha a descrever o que esta flag faz", dest="text", type=str)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()