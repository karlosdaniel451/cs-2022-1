#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.animal import Animal

@dataclass
class Cavalo(Animal):
    def emitir_som(self) -> None:
        print('CAVALO! (Imagine o sonoplasta do Rodrigo Faro.)')

    def correr(self) -> None:
        print(f'Sou {self.nome} e estou correndo como um cavalo.')

