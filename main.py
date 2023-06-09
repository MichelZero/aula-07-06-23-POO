#
#
# autor: Michel
#
# data: 09/06/2023

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
print(calc1.IMC())