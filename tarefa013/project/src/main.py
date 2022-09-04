from src.bairro import Bairro
from src.cidade import Cidade
from src.endereco import Endereco, TipoEndereco
from src.estado import Estado
from src.logradouro import Logradouro, TipoLogradouro
from src.pais import Pais


def main():
    brasil = Pais('Brasil')
    goias = Estado('GO', 'Goiás', brasil)
    goiania = Cidade('Goiânia', goias)
    chacaras_california = Bairro('Chácaras Califórnia', goiania)
    alameda_palmeiras = Logradouro('Alameda Palmeiras', TipoLogradouro.ALAMEDA)
    endereco_do_INF = Endereco(
        0,
        74690900,
        TipoEndereco.COMERCIAL,
        chacaras_california,
        'Quadra d',
        alameda_palmeiras
    )

    print(endereco_do_INF.numero)
    print(endereco_do_INF.bairro)
    print(endereco_do_INF.bairro.cidade)
    print(endereco_do_INF.bairro.cidade.estado)
    print(endereco_do_INF.bairro.cidade.estado.pais)


if __name__ == '__main__':
    main()
