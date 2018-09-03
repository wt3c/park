
# Capítulo 2

### Strings e textos

##### 2.2 - Fazer correspondência de texto no inicio ou fim de uma string



```python
# Maneira simples de verificar o inicio ou o fim de uma string]
# str.startswith() str.endswith()

file = 'spam.txt'
url = 'http://www.python.org.br'
print(file.startswith('s'))
print(file.endswith('.txt'))

print(url.startswith('http'))
print(url.endswith('.org.br'))
print(url.endswith('.ca'))
```

    True
    True
    True
    True
    False



```python
import os 
filenames = os.listdir('.')

print(filenames)
```

    ['capitulo1-estruturas_ de_dados_e_algoritmos.ipynb', '__init__.py', 'test.py', '.ipynb_checkpoints', 'somefile.txt', 'capitulo2-string_e_texto.ipynb', 'somefile.txt~']



```python
names = [name for name in filenames if name.endswith('txt')]
print(names)
```

    ['somefile.txt']


###### Busca por vários tipos de arquivos


```python
print(any(name.endswith('ipynb') for name in filenames))
```

    True



```python
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http', 'https', 'ftp')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
```


```python
choices = ['http', 'ftp']
url = 'http://www.python.org'
print(url.startswith(choices))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-12f15bf9e78f> in <module>()
          1 choices = ['http', 'ftp']
          2 url = 'http://www.python.org'
    ----> 3 print(url.startswith(choices))
    

    TypeError: startswith first arg must be str or a tuple of str, not list



```python
choices = ['http', 'ftp']
url = 'http://www.python.org'
print(url.startswith(tuple(choices)))
```

    True


Também podemos pesquisar por meio de "FATIAS" EX.: file[-4:], porem é menos elegante


##### 2.3 Fazer corrspondências de strings utilizando padrões de curinga do shell

* *.py, Dat[0-9]*.csv 

$$e^x=\sum_{i=0}^\infty \frac{1}{i!}x^i$$

Não é nada, só por que eu posso!


```python
# O modulo fnmtach disponibiliza recusos para esse uso

from fnmatch import fnmatch, fnmatchcase
```


```python
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?00.txt'))
print(fnmatch('foo.txt', '?oo.txt'))

```

    True
    False
    True



```python
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

pprint([name for name in names if fnmatch(name, 'Dat*.csv')])
```

    ['Dat1.csv', 'Dat2.csv']


<font color=red>Fnmatch NÃO é case sensitive. Caso for necessário o uso de case sensitive, utilize fnmatchcase    
    
</font>


*** 





```python
print(fnmatchcase('foo.txt', '*.TXT'))
```

    False



```python
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]
```


```python
from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST' )])
```

    ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']


##### 2.4 Matching e pesquisa de padrões de texto


```python
text = 'yeah, but no, but yeah, but no, but yeah'

# Match exato
print(text == 'yeah')

# Correspondência no início ou no final
print(text.startswith('yeah'))
print(text.endswith('no'))

# Procurar pela localização da primeira ocorrência
text.find('no')


```

    False
    True
    False





    10




```python
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

    
```

    yes
    no


- Pré-compilar o padrão para reutiliza-lo 
***


```python
datepat = re.compile(r'\d+/\d+/\d+')
```


```python
if datepat.match(text1):
    print('É nós !!!')
else:
    print('Não deu !!!')
```

    É nós !!!



```python
if datepat.match(text2):
    print('É nós !!!')
else:
    print('Não deu !!!')
```

    Não deu !!!


- Pesquisando em toda a ocorrência de um padrão
***


```python
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)
```




    ['11/27/2012', '3/13/2013']




```python
# criando grupo de padão
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
```


```python
m = datepat.match('11/27/2012')
print(m)

```

    <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>



```python
print('m.group(0) ==>', m.group(0))
print('m.group(1) ==>', m.group(1))
print('m.group(2) ==>', m.group(2))
print('m.group(3) ==>', m.group(3))
print('m.groups() ==>', m.groups())
```

    m.group(0) ==> 11/27/2012
    m.group(1) ==> 11
    m.group(2) ==> 27
    m.group(3) ==> 2012
    m.groups() ==> ('11', '27', '2012')



```python
# Olha a Tupla ae gente...
month, day, year = m.groups() # lindo isso...

print(month, 'month')
print(year, 'year')
print(day, 'day')

```

    11 month
    2012 year
    27 day



```python
print(datepat.findall(text))
```

    [('11', '27', '2012'), ('3', '13', '2013')]



```python
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(day, month, year))
```

    27-11-2012
    13-3-2013



```python
# findall sempre retorna uma lista. Para encontrar um match iteravelemente, usamos o finditer
for m in datepat.findall(text):
    print(m)
```

    ('11', '27', '2012')
    ('3', '13', '2013')



```python
for i in datepat.finditer(text):
    print(i.groups())
    print(i.group(2), i.group(1), i.group(3))  
```

    ('11', '27', '2012')
    27 11 2012
    ('3', '13', '2013')
    13 3 2013


***
- O método match() verifica somente inicio da string podendo trazer informoções indesejadas. Para um matching mas apurado, inclua o marcador '$' no final da expressão.
***



```python
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
```


```python
datepat.match('11/27/2012abcdef')
```




    <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>




```python
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
```


```python
print(datepat.match('11/27/2012abcdef'))
```

    None



```python
datepat.match('11/27/2012')
```




    <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>




```python
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
```

    [('11', '27', '2012'), ('3', '13', '2013')]


***
##### 2.5 Pesquisar e substituir textos
***

