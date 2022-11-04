"""
dict={'ana':8}
dict['joao'] = 170
a=1
b=2
c=3
e=5
x=(a,b,c)
dict[e]= x
print(dict)
info=dict()
user=list()
for c in range(0,2):
    info['nome']=str(input('Usuário:'))
    info['email']=str(input('email user:'))
    user.append(info.copy())

for e in user:
  for k, v in e.items():
    print(f' nome:{k} usuário{v}')

#------------------Leitura de Dados----------------------------------

print('Preencha os campos abaixo com o horário atual')

h = int(input('Hora: '))

m = int(input('Minuto: '))

s = int(input('Segundo: '))




#----Determinação do Horário de Término do Evento---


#----Apresentação do Horário de Término do Evento---

print(f'O fim do evento se dará às {h}h {m}min e {s} segundos')

#-----------------Fim do Programa-------------------------------------

from datetime import datetime as bra
horario = bra.time(bra.now())
print(f'O horátio agora é {horario}')
"""
from datetime import time

a = time(12, 30, 0)

print("Hora =", a.hour)
print("Minuto =", a.minute)
print("Segundo =", a.second)
print("Microssegundo =", a.microsecond)