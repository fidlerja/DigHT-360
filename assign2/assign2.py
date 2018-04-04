''' Adam Fidler
    Assignment 2
    DIGHT 360
    '''
import re

input_file = open('text.txt', 'r')
text = input_file.read()

ger_re = r'\w{1,}[^Eyr|Beij]ing\b'
agent_re = r'\w{2,}or(?:\b|s\b)'
rec_re = r'\w{3,}ee(?:\b|s\b)'

ger_find = re.findall(ger_re, text)
print(ger_find, len(ger_find))

agent_find = re.findall(agent_re, text)
print(agent_find, len(agent_find))

rec_find = re.findall(rec_re, text)
print(rec_find, len(rec_find))

