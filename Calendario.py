import calendar
import os
class Calendario:
  def __init__(self, ano, mes, dia):
     self.ano=ano
     self.mes=mes
     self.dia=dia

  def consultar_calendario(self):
       desejo=input("Deseja consultar calendário: ")
       if desejo=='sim':
          print(calendar.calendar(2022))
       elif desejo =='não' or desejo=='nao':
          pass
                   
  def calendario(self):
      deseja = input('Deseja criar alguma atividade?\nR: ')
      if deseja == 'sim':
        atividade = input('Digite o nome da atividade: ')
        mes=int(input("Digite o número do mês que deseja agendar: "))
        dia=int(input("Digite o dia do mês que deseja: "))
        ano=int(input('Digite o ano que deseja: '))
        calendario=ano,mes,dia
        print(f'Você agendou "{atividade}" para: {dia}/{mes}/{ano}')
        file = open ('cadastros.txt', 'a+')
        file.write ("%s, %s, %s, %s\n" %(atividade, dia, mes, ano))
        os.system('clear')
        try:
          agenda= open("agenda.txt","a")
          dados= f'A atividade "{atividade}" foi marcada para:{dia}/{mes}/{ano}'
          agenda.write(dados)
          agenda.close()
          print("Informações salvas com sucesso")
        except:
          print("ERRO NO AGENDAMENTO")
        

var= Calendario("","","")
var.consultar_calendario()
var.calendario()