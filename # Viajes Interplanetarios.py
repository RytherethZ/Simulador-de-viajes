# Viajes Interplanetarios

class Planeta:
    total_planetas = 0  # variable de clase para el conteo

    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia  # millones de km
        Planeta.total_planetas += 1

    def __del__(self):
        Planeta.total_planetas -= 1
        print(f"[Destructor] Planeta {self.nombre} eliminado")

    @classmethod
    def total(cls):
        return cls.total_planetas

    def mostrar(self):
        print(f"Planeta: {self.nombre} | Distancia: {self.distancia} millones km")


class NaveEspacial:
    total_naves = 0

    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad  # millones km por día
        self.destino = None
        self.misiones = []
        self.recursos = {}
        NaveEspacial.total_naves += 1

    def __del__(self):
        NaveEspacial.total_naves -= 1
        print(f"[Destructor] Nave {self.nombre} eliminada")

    @classmethod
    def total(cls):
        return cls.total_naves

    def asignar_destino(self, planeta):
        self.destino = planeta
        print(f"Nave {self.nombre} -> destino {planeta.nombre}")

    def tiempo_viaje(self):
        if self.destino is None:
            print("La nave no tiene destino asignado")
        else:
            t = self.destino.distancia / self.velocidad
            print(f"Tiempo de viaje: {t:.2f} días")

    def agregar_misiones(self, *misiones):  # *args
        self.misiones.extend(misiones)

    def cargar_recursos(self, **recursos):  # **kwargs
        self.recursos.update(recursos)

    def mostrar(self):
        d = self.destino.nombre if self.destino else "Ninguno"
        print(f"Nave: {self.nombre} | Velocidad: {self.velocidad} | Destino: {d}")
        print(f"  Misiones: {self.misiones} | Recursos: {self.recursos}")


planetas = []  # variables globales
naves = []

while True:
    print("\n=== MENÚ ===")
    print("1. Registrar planeta")
    print("2. Registrar nave")
    print("3. Asignar destino")
    print("4. Calcular tiempo de viaje")
    print("5. Mostrar información")
    print("6. Salir")
    opc = input("Opción: ")

    if opc == "1":
        nombre = input("Nombre del planeta: ")
        dist = float(input("Distancia (millones km): "))
        planetas.append(Planeta(nombre, dist))

    elif opc == "2":
        nombre = input("Nombre de la nave: ")
        vel = float(input("Velocidad (millones km/día): "))
        nave = NaveEspacial(nombre, vel)
        nave.agregar_misiones("explorar", "mapear")          # ejemplo *args
        nave.cargar_recursos(oxigeno=100, agua=50)           # ejemplo **kwargs
        naves.append(nave)

    elif opc == "3":
        for i, p in enumerate(planetas): print(i + 1, p.nombre)
        ip = int(input("Número de planeta: ")) - 1
        for i, n in enumerate(naves): print(i + 1, n.nombre)
        inn = int(input("Número de nave: ")) - 1
        naves[inn].asignar_destino(planetas[ip])

    elif opc == "4":
        for i, n in enumerate(naves): print(i + 1, n.nombre)
        inn = int(input("Número de nave: ")) - 1
        naves[inn].tiempo_viaje()

    elif opc == "5":
        print(f"Total planetas: {Planeta.total()} | Total naves: {NaveEspacial.total()}")
        for p in planetas: p.mostrar()
        for n in naves: n.mostrar()

    elif opc == "6":
        planetas.clear()  # libera los objetos y dispara los destructores
        naves.clear()
        print("Sistema cerrado.")
        break