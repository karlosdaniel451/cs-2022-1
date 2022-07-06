#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

from src.animal import Animal

@dataclass
class Preguica(Animal):
    def emitir_som(self) -> None:
        print(f'Sou {self.nome} e estou emitindo sons de preguiças.')

    def subir_em_arvore(self) -> None:
        print(f'Sou {self.nome} e estou subindo em árvore.')

