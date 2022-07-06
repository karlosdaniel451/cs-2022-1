from src.animal import Animal

def main():
    examinar()


def examinar(animal: Animal):
    animal.emitir_som()


if __name__ == '__main__':
    main()
