from auto import Auto # Importa la clase Auto desde el archivo auto.py
from moto import Moto # Importa la clase Moto desde el archivo moto.py
from camion import Camion # Importa la clase Camion desde el archivo camion.py

vehiculo1 = Auto("AB1234", 2018) # Instancia el objeto Auto pasándole su patente y año
vehiculo2 = Moto("CD5678", 2020) # Instancia el objeto Moto pasándole su patente y año
vehiculo3 = Camion("EF9012", 2023) # Instancia el objeto Camion pasándole su patente y año

print(vehiculo1.ingresar()) # Ejecuta ingresar() del primer vehículo y muestra el texto retornado en consola
print(vehiculo2.ingresar()) # Ejecuta ingresar() del segundo vehículo y muestra el texto retornado en consola
print(vehiculo3.ingresar()) # Ejecuta ingresar() del tercer vehículo y muestra el texto retornado en consola

print(f"Tarifa por hora del primer vehículo: ${vehiculo1.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el primer vehículo
print(f"Tarifa por hora del segundo vehículo: ${vehiculo2.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el segundo vehículo
print(f"Tarifa por hora del tercer vehículo: ${vehiculo3.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el tercer vehículo
