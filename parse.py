import re

with open('a.html', mode='r', encoding='utf-8') as html:
    page = html.read()

h3 = re.findall(r'id="name_[0-9]+".*?.*?.*?>[A-Za-z]+</a>', page)

clean = [n.split('>')[1].split('<')[0] for n in h3]


output = ''

for x in clean:
    output += x + '\n'

with open('usrmo02.txt', 'w') as ub:
    ub.write(output)

