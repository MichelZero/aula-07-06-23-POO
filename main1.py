#
#
# autor: Michel
#
# data: 07/06/2023

# importando a classe Pessoa.
from pessoa import Pessoa as P



# criando os objetos do tipo pessoa
p1 = P()

# chamando os métodos
print(f"nome original é {p1.nome}")
p1.trocaNome("Davi")
print(f"novo nome é {p1.nome}")
print(f"novo nome é {p1.informeNome()}")

