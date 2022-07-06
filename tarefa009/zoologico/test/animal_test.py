#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.animal import Animal
from src.cachorro import Cachorro
from src.cavalo import Cavalo
from src.preguica import Preguica

def main():
    cachorro = Cachorro(nome='Rex', idade=5)
    emitir_som(animal=cachorro)

    cavalo = Cavalo(nome='Alex', idade=7)
    emitir_som(animal=cavalo)

    preguica = Preguica(nome='Jane', idade=6)
    emitir_som(animal=preguica)


def emitir_som(animal: Animal):
    animal.emitir_som()


if __name__ == '__main__':
    main()

