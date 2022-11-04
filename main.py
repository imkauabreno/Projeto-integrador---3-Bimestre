import os
print('oi')
from Usuario import*
deseja = input('\nOlá, deseja ir ao painel de agendamentos?\nResposta: ')
os.system('clear')
if deseja == 'sim':
  from Calendario import *
else:
  exit()