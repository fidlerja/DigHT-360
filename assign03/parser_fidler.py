import re

with open('wiki.html', 'r') as my_file,\
        open('wiki_parsed.txt', 'w') as new_file:
        my_REa = r'<li.*?><a .*?>(?:<span.*<bdi .*?>)?'
        my_REb = r'(?:<bdi.*?>)?(.*?)(?:</bdi>)?</a></li>'
        my_RE = my_REa + my_REb
        lang_matches = re.findall(my_RE, my_file.read())
        for lang in lang_matches:
            print(lang, file=new_file)
print('')

