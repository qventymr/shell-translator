#!/usr/bin/env python3

from translate import Translator
import argparse
from langdetect import detect, detect_langs
from langdetect.lang_detect_exception import LangDetectException


def detect_language(text):
    try:
        lang = detect(text)
        
        languages = detect_langs(text)
        
        return lang
    except LangDetectException as e:
        return None, str(e)

def auto_translate(text, target_lang):
    try:
        source_lang = detect_language(text)
        
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text)
        
        return translation
        
    except Exception as e:
        return None, None, f"Error: {e}"



parser = argparse.ArgumentParser(description='Shell translator')
parser.add_argument('text', help='Text to translate')
parser.add_argument('-l','--lang', help='Target Language', required=True)
args = parser.parse_args()

print(auto_translate(text=args.text, target_lang=args.lang))

