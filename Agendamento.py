class Agendamento:
  def __init__(self,titulo, descricao,notas):
    self.titulo = None
    self.descricao = None
    self.notas = None
    
  def criarAgendamento(self):
   from Calendario import *
   self.titulo=input(str("Título do agendamento: "))
   self.descricao=input(str("Descrição do agendamento: "))
   self.notas=input("Comentário: ")
      
  def deletarAgendamento(self):
    self.titulo = None
    self.descricao = None
    self.notas = None
    print ('Seu agendamento foi deletado!')
    
class Eventos(Agendamento):
  def __init__(self, notas, titulo, descricao, notificacao):
    se.()__init__(notas, titulo, descricao)
    self.notificacao = None
#metodo exibir atividade
  def exibir_Atividade(self):
    from Calendario import *
    self.notificacao = print(f' Você agendou "{atividade}" para: {dia}/{mes}/{ano}')
  
   #importar input (metodo) de definir data, da classe calendario.
   #importar input (metodo) de definir hora, da classe calendario.
#subclasses eventos e atividades