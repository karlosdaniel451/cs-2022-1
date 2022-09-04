from conta_bancaria import ContaBancaria
from exceptions.saldo_insuficiente_error import SaldoInsuficienteError

def main():
    conta_1 = ContaBancaria(5_000)
    conta_2 = ContaBancaria(500)

    conta_1.sacar(1_000)
    try:
        conta_2.sacar(1_000)
    except SaldoInsuficienteError as error:
        print(f'Erro: {error.message}')


if __name__ == '__main__':
    main()
