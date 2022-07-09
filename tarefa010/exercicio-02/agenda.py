from .contato import Contato

class Agenda:
    def _init__(self):
        self._contatos: list[Contato] = []

    def adicionar_contato(self, contato: Contato):
        """Adiciona um contato na lista de contatos."""
        self._contatos.append(contato)

    def buscar_contato_por_nome(self, nome: str) -> Contato:
        """Busca um contato da lista de contatos por nome."""
        for contato in self._contatos:
            if contato.nome == nome:
                return contato


    def buscar_contato_por_email(self, email: str) -> Contato:
        """Busca um contato da lista de contatos por email."""
        for contato in self._contatos:
            if contato.email == email:
                return contato

    def remover_contato_por_nome(self, nome: str):
        """Remove um contato da lista de contatos por nome."""
        for index, contato in enumerate(self._contatos):
            if contato.nome == nome:
                return self._contatos.pop(index)
        
        raise ValueError('Não existe nenhum contato com tal nome.')

    def remover_contato_por_nome(self, email: str):
        """Remove um contato da lista de contatos por email."""
        for index, contato in enumerate(self._contatos):
            if contato.nome == email:
                return self._contatos.pop(index)
        
        raise ValueError('Não existe nenhum contato com tal email.')

    def lista_contatos(self) -> str:
        """Lista os contatos presentes na lista de contatos."""
        return self._contatos