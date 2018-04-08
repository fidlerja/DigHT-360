import re
import nltk
from glob import glob

master_list = []
master_list.append(glob('../Mini-CORE/1+IN*.txt'))
master_list.append(glob('../Mini-CORE/1+IP*.txt'))
master_list.append(glob('../Mini-CORE/1+LY*.txt'))
master_list.append(glob('../Mini-CORE/1+NA*.txt'))
master_list.append(glob('../Mini-CORE/1+OP*.txt'))
master_list.append(glob('../Mini-CORE/1+SP*.txt'))

feat_list = []
feat_list.append(re.compile(r'"\w.*"'))
feat_list.append(re.compile(r'(\w*\'[^sA-Z ])|([Cc]horus)'))
long_re = r'(I\W)|([Yy]ou\W)|(\b[Ss]?[Hh]e\W)|([[Ww]e\W)|([Tt]hey)'
feat_list.append(re.compile(long_re))

results = []
print('filename', 'Quotes', 'Contractions', 'Pronouns', 'register', sep=',')
for item in master_list:
    for text in item:
        with open(text, 'r') as filename:
            contents = filename.read()
            contents = re.sub(r'<.*>', '', contents)
            print(str(filename)[25:29] + '...', end='')
            print(str(filename)[62:73], end=',')
            for feature in feat_list:
                occurences = feature.findall(contents)
                total_occs = len(occurences)
                total_toks = len(nltk.word_tokenize(contents))
                norm = round(total_occs/(total_toks/1000), 3)
                print(norm, end=',')
            print(str(filename)[27:29])

'''
IN: Informational (Wikipedia)

IP: Informational Persuasion

LY: Song Lyrics

NA: News reports

OP: Opinion blogs

SP: Interview transcripts
'''
