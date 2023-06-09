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
    # arredondando o resultado para duas casas decimais.
    # chamando o método classificacao() dentro do método IMC()
    return classificacao(self)
  
  # criando o método para retornar a classificação do IMC.
  def classificacao(self):
    if self.IMC() < 18.5:
      return "abaixo do peso normal!"
    elif self.IMC() >= 18.5 and self.IMC() <= 24.9:
      return "peso normal!"
    elif self.IMC() >= 25.0 and self.IMC() <= 29.9:
      return "excesso de peso!"
    elif self.IMC() >= 30.0 and self.IMC() <= 34.9:
      return "obesidade classe I"
    elif self.IMC() >= 35.0 and self.IMC() <= 39.9:
      return "obesidade classe II"
    elif self.IMC() >= 40 :
      return "obesidade classe III"
    else:
      return "dados errados"
    