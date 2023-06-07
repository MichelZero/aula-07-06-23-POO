#
#
# autor: Michel
#
# data: 07/06/2023

# criar a classe Pessoa.
class Pessoa():
  nome = None
  DataNascimento = ''
  CPF = ''
  
  
  def trocaNome(self, valor):
    self.nome = valor
  
  def informeNome(self):
    return self.nome
    
  def trocaData(self, valor):
    self.DataNascimento = valor
    
  def trocaCPF(self, valor):
    self.CPF = valor