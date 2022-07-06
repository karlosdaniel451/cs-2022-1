#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class Animal():
    nome: str
    idade: int

    def emitir_som(self) -> None:
        pass

