#
#
# autor: Michel
#
# data: 07/06/2023

# importando a classe CalculadoraIMC
from calcIMC import CalculadoraIMC as CIMC

# criando o objeto CalculadoraIMC
calc1 = CIMC()

# entrada de dados
peso = int(input("informe o peso: "))
altura = float(input("informe a altura: "))
#
calc1.setPeso(peso)
calc1.setAltura(altura)
#print(calc1.IMC())

# https://endocrinologiacuritiba.com.br/wp-content/uploads/2012/02/tabela_imc.jpg
if calc1.IMC() < 18.5:
  print("abaixo do peso normal!")
elif calc1.IMC() >= 18.5 and calc1.IMC() <= 24.9:
  print("peso normal!")
elif calc1.IMC() >= 25.0 and calc1.IMC() <= 29.9:
  print("excesso de peso!")
elif calc1.IMC() >= 30.0 and calc1.IMC() <= 34.9:
  print("obesidade classe I")
elif calc1.IMC() >= 35.0 and calc1.IMC() <= 39.9:
  print("obesidade classe II")
elif calc1.IMC() >= 40 :
  print("obesidade classe III")
else:
  print("dados errados")