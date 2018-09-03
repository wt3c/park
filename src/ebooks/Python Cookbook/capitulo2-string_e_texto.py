
# coding: utf-8

# # Capítulo 2
# 
# ### Strings e textos

# ##### 2.2 - Fazer correspondência de texto no inicio ou fim de uma string

# In[1]:


# Maneira simples de verificar o inicio ou o fim de uma string]
# str.startswith() str.endswith()

file = 'spam.txt'
url = 'http://www.python.org.br'
print(file.startswith('s'))
print(file.endswith('.txt'))

print(url.startswith('http'))
print(url.endswith('.org.br'))
print(url.endswith('.ca'))


# In[2]:


import os 
filenames = os.listdir('.')

print(filenames)


# In[4]:


names = [name for name in filenames if name.endswith('txt')]
print(names)


# ###### Busca por vários tipos de arquivos

# In[5]:


print(any(name.endswith('ipynb') for name in filenames))


# In[6]:


from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http', 'https', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


# In[7]:


choices = ['http', 'ftp']
url = 'http://www.python.org'
print(url.startswith(choices))


# In[8]:


choices = ['http', 'ftp']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))


# Também podemos pesquisar por meio de "FATIAS" EX.: file[-4:], porem é menos elegante
# 

# ##### 2.3 Fazer corrspondências de strings utilizando padrões de curinga do shell
# 
# * *.py, Dat[0-9]*.csv 

# $$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$$
# 
# Não é nada, só por que eu posso!

# In[10]:


# O modulo fnmtach disponibiliza recusos para esse uso

from fnmatch import fnmatch, fnmatchcase


# In[14]:


print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?00.txt'))
print(fnmatch('foo.txt', '?oo.txt'))


# In[28]:


names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

pprint([name for name in names if fnmatch(name, 'Dat*.csv')])


# <font color=red>Fnmatch NÃO é case sensitive. Caso for necessário o uso de case sensitive, utilize fnmatchcase    
#     
# </font>
# 

# *** 
# 
# 
# 

# In[29]:


print(fnmatchcase('foo.txt', '*.TXT'))


# In[31]:


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]


# In[33]:


from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST' )])


# ##### 2.4 Matching e pesquisa de padrões de texto

# In[41]:


text = 'yeah, but no, but yeah, but no, but yeah'

# Match exato
print(text == 'yeah')

# Correspondência no início ou no final
print(text.startswith('yeah'))
print(text.endswith('no'))

# Procurar pela localização da primeira ocorrência
text.find('no')


# In[44]:


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# Correspondência simples: \d+ significa corresponder a um ou mais dígitos

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
    
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

    


# - Pré-compilar o padrão para reutiliza-lo 
# ***

# In[45]:


datepat = re.compile(r'\d+/\d+/\d+')


# In[46]:


if datepat.match(text1):
    print('É nós !!!')
else:
    print('Não deu !!!')


# In[47]:


if datepat.match(text2):
    print('É nós !!!')
else:
    print('Não deu !!!')


# - Pesquisando em toda a ocorrência de um padrão
# ***

# In[48]:


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)


# In[49]:


# criando grupo de padão
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


# In[50]:


m = datepat.match('11/27/2012')
print(m)


# In[53]:


print('m.group(0) ==>', m.group(0))
print('m.group(1) ==>', m.group(1))
print('m.group(2) ==>', m.group(2))
print('m.group(3) ==>', m.group(3))
print('m.groups() ==>', m.groups())


# In[55]:


# Olha a Tupla ae gente...
month, day, year = m.groups() # lindo isso...

print(month, 'month')
print(year, 'year')
print(day, 'day')


# In[58]:


print(datepat.findall(text))


# In[62]:


for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(day, month, year))


# In[68]:


# findall sempre retorna uma lista. Para encontrar um match iteravelemente, usamos o finditer
for m in datepat.findall(text):
    print(m)


# In[77]:


for i in datepat.finditer(text):
    print(i.groups())
    print(i.group(2), i.group(1), i.group(3))  


# ***
# - O método match() verifica somente inicio da string podendo trazer informoções indesejadas. Para um matching mas apurado, inclua o marcador '$' no final da expressão.
# ***
# 

# In[94]:


datepat = re.compile(r'(\d+)/(\d+)/(\d+)')


# In[95]:


datepat.match('11/27/2012abcdef')


# In[96]:


datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')


# In[99]:


print(datepat.match('11/27/2012abcdef'))


# In[100]:


datepat.match('11/27/2012')


# In[102]:


print(re.findall(r'(\d+)/(\d+)/(\d+)', text))


# ***
# ##### 2.5 Pesquisar e substituir textos
# ***
# 
