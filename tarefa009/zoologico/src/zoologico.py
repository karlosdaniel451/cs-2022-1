from dataclasses import dataclass, field

from src.animal import Animal
from src.cachorro import Cachorro
from src.cavalo import Cavalo
from src.preguica import Preguica

@dataclass
class Zoologico():
    jaulas: list[Animal] = field(init=False, default_factory=list)

    def __init__(self):
        # self.jaulas = [None for _ in range(10)]

    # def add_animal_em_jaula(self, animal: Animal, numero_da_jaula: int):
    #     if numero_da_jaula < 0 or numero_da_jaula > 9:
    #         raise ValueError('cage_number must be between 0 and 9.')

    #     self.jaulas[numero_da_jaula] = animal

    def add_animal_em_jaula(self, animal: Animal):
        self.jaulas.append(animal)
    
    def __str__(self):
        return str(self.jaulas)


def main():
    zoologico = Zoologico()

    for i in range(4):
        zoologico.add_animal_em_jaula(animal=Cachorro(nome=f'Cachorro {i+1}', idade=i))
    
    for i in range(4, 7):
        zoologico.add_animal_em_jaula(animal=Cavalo(nome=f'Cavalo {i-3}', idade=i-3))

    for i in range(7, 10):
        zoologico.add_animal_em_jaula(animal=Preguica(nome=f'Preguiça {i-6}', idade=i-3), numero_da_jaula=i)

    for cage in zoologico.jaulas:
        cage.emitir_som()

        if isinstance(cage, Cachorro) or isinstance(cage, Cavalo):
            cage.correr()
            print()


if __name__ == '__main__':
    main()
