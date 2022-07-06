#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.animal import Animal

@dataclass
class Cachorro(Animal):
    def emitir_som(self) -> None:
        print(f'Sou {self.nome} e estou emitindo sons de cachorros.')

    def correr(self) -> None:
        print(f'Sou {self.nome} e estou correndo como um cachorro.')

