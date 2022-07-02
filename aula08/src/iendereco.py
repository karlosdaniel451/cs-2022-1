from abc import ABC, abstractmethod

class IEndereco(ABC):

    @abstractmethod
    def consultar_por_cep(self):
        pass
