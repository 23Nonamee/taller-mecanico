class Vehiculo:
    def __init__(self, patente: str, anio : int, modelo: str):
        self.patente = patente
        self.anio = anio 
        self.modelo = modelo
        self.__en_taller: bool = False

    def ingresar(self) -> str :
        if self.__en_taller: 
            return "El vehiculo ya esta en el taller"
        
        self.__en_taller = True
        return "El vehiculo ha sido ingresado"

    def entregar(self) -> str:
        if not self.__en_taller:
            return "El vehiculo no esta en el taller"
        self.__en_taller = False
        return "El vehiculo ha sido entregado"
    
    def tarifa_hora(self) -> int:
        return 5000

    def mostrar_auto(self):
        print(f"patente: {self.patente}")
        print(f"anio: {self.anio}")
        print(f"modelo: {self.modelo}")
     
        
