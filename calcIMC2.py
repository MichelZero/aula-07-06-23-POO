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
    # dividindo a altura por 100 para converter para metros
    self.altura = self.altura / 100
    # calculando o IMC
    resultado = self.peso / self.altura ** 2
    # retornando o resultado com duas casas decimais
    return round(resultado, 2)
  
  # criando o método para retornar a classificação do IMC.
  def classificacao(self):
    # chamando o método IMC() para calcular o IMC
    IMC = self.IMC()
    # retornando a classificação
    if IMC < 18.5:
      return "abaixo do peso normal!"
    elif IMC >= 18.5 and IMC <= 24.9:
      return "peso normal!"
    elif IMC >= 25.0 and IMC <= 29.9:
      return "excesso de peso!"
    elif IMC >= 30.0 and IMC <= 34.9:
      return "obesidade classe I"
    elif IMC >= 35.0 and IMC <= 39.9:
      return "obesidade classe II"
    elif IMC >= 40 :
      return "obesidade classe III"
    else:
      return "dados errados"
    