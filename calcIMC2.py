#
#
# autor: Michel
#
# data: 09/06/2023

# criar a classe CalculadoraIMC.
class CalculadoraIMC():
  altura = None
  peso = None
  
  def setAltura(self, valor):
    self.altura = valor
    
  def setPeso(self, valor):
    self.peso = valor
    
  def IMC(self):
    resultado = self.peso / self.altura ** 2
    return resultado