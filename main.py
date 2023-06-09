#
#
# autor: Michel
#
# data: 09/06/2023

# importando a classe CalculadoraIMC do arquivo calcIMC2.py
from calcIMC2 import CalculadoraIMC as CIMC

# criando o objeto CalculadoraIMC
calc1 = CIMC()

# entrada de dados
peso = int(input("informe o peso: "))
# ajustei o tipo para int e dentro do método IMC() fiz a conversão para metros
altura = int(input("informe a altura: "))
#
calc1.setPeso(peso)
calc1.setAltura(altura)
print(calc1.IMC())

print(f"você está {calc1.classificacao()}")