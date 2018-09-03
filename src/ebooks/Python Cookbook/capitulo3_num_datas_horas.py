
# coding: utf-8

# # Capítulo 3
# 
# ## Números, datas e horas

# In[2]:


print(round(1.27, 1))
print(round(-1.24, 1))
print(round(1.32564675, 3))


# In[3]:


# O comportamento do arrendondamento consiste em aarrendondar para o dígito mais próximo
print(round(1.5))
print(round(2.5)) # Porque não arrendondou para 3 ?
print(round(3.5))


# In[4]:


# round <> de formatação de saida

x = 1.125456
print(format(x, '0.3f'))
print(round(x, 3))


# ##### 3.2. Realizar cálculos decimais precisos
# 
# Um problema bem conhecido com números de ponto flutuante, é que não são capazes de representar todos os decimais de base 10. Além do mais, cáculos simples podem gerar erros.

# In[6]:


a = 4.2
b = 2.1

print(a + b)
print(a + b == 6.3)


# Esses erros são uma limitação da CPU subjacente e da aritimética 754 do IEEE executada pela sua unidade de ponto flutuante. Se o codigo for feito com instâncias de float, não tem o que fazer em relação a esse erro, pois o Python utiza representação nativa para armazenar os dados.
# 
# Uma solução para esse problema é o módulo decimal.
# 
# Mais como nada é de graça, com o uso do decimal ganhamos precição mas perdemos desempenho.

# In[16]:


from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')

print(a + b)
(a + b) == Decimal('6.3')


# ##### 3.3 Formatar números para saida

# In[17]:


x = 1234.57689

# Precisão de duas casas decimais

format(x, '0.2f')


# In[18]:


# Justificando à direta com 10 caracteres e precisão de um digíto
format(x, '>10.1f')


# In[19]:


# À esquerda
format(x, '<10.1f')


# In[20]:


# Centro
format(x, '^10.1f')


# In[22]:


# Inclusão de separador de milhares
format(x, ',')


# In[23]:


format(x, '0,.1f')


# ##### 3.12 Converter dias para segundos e outras conversões básicas relacionadas  com tempo

# In[28]:


from datetime import timedelta


# In[33]:


a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b 

print('a : ', a)
print('b : ', b)


# In[34]:


c.days


# In[35]:


c.seconds


# In[36]:


c.seconds / 3600


# In[37]:


c.total_seconds() / 3600


# In[40]:


# Operações aritimeticas com DATAS

from datetime import datetime

a = datetime(2018, 8, 21)
print('a : ', a)


# In[43]:


print(a + timedelta(days=10))


# In[45]:


b = datetime(2018, 12, 21)
d = b - a

d.days


# In[46]:


now = datetime.today()
print(now)


# In[48]:


print(now + timedelta(minutes=10))


# #### 3.13 Determinar o dia da última sexta-feira
# 

# In[14]:


from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
        
    return target_date


# In[16]:


datetime.today()


# In[18]:


get_previous_byday('Monday')


# In[19]:


get_previous_byday('Friday')


# #### 3.14 - Encontrar o intervalo de datas do mês corrente

# In[1]:


from datetime import date, datetime, timedelta
import calendar


# In[21]:


def  get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    
    print("Calendar.monthrange(year, month), # Retorna quandidade de dias no mês")
    print(calendar.monthrange(start_date.year, start_date.month)) 
    print()
    
    
    return(start_date, end_date)


# In[22]:


a_day = timedelta(days=1)
first_day, last_day =  get_month_range(date.today())

while first_day < last_day:
    print(first_day)
    first_day += a_day


# In[26]:


# Usando um gerador(iteravel) - yield
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


# In[27]:


# Exibir a data no intervalo de 6 horas
# date_range é um interavél (yield)
for d in date_range(datetime(2012, 9, 1),datetime(2012,10,1), timedelta(hours=6)):
    print(d)  


# In[32]:


# parser + um formato entre datas
import dateutil.parser
d = dateutil.parser.parse('2018-09-02T18:38:15.3601734Z')
print(d.strftime('%d/%m/%Y'))


# #### 3.15 - Converter strings em datetimes

# In[34]:


text = '2012-09-20'

y =  datetime .strptime(text, '%Y-%M-%d')
z = datetime.now()
diff = z-y
diff


# In[35]:


z


# In[36]:


nice_z = datetime.strftime(z, "%A %B %d, %Y")
nice_z

