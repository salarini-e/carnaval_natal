from django.utils.regex_helper import _lazy_re_compile
import re

re_words = _lazy_re_compile(r'<[^>]+?>|([^<>\s]+)', re.S)
re_chars = _lazy_re_compile(r'<[^>]+?>|(.)', re.S)
re_tag = _lazy_re_compile(r'<(/)?(\S+?)(?:(\s*/)|\s.*?)?>', re.S)
re_newlines = _lazy_re_compile(r'\r\n|\r')  # Used in normalize_newlines
re_camel_case = _lazy_re_compile(r'(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))')

def separarLinhas(v):
    value = normalize_newlines(v)
    paras = re.split('\n{2,}', str(value))
    return paras 

def normalize_newlines(text):    
    return re_newlines.sub('\n', str(text))