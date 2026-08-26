from vehiculo import Vehiculo

def main():

    auto = Vehiculo("21342", 2015, "Yaris")

    entregar = auto.entregar()
    print(entregar)

    mostrar = auto.mostrar_auto()
    print(mostrar) 


if __name__ == "__main__":
    main()