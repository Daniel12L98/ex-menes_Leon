class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = "peruana"

    def mostrar_saldo(self):
        print("El saldo actual de {} es: {}".format(self.nombre, self.saldo))


    def transferencia(self, persona_2,monto):
        if self.saldo >= monto:
            self.saldo -= monto
            persona_2.saldo += monto
        else:
            print("El saldo que tienes es insuficiente")
# persona 1

persona_1 = Persona("Pedro", 45, 3000)
persona_2 = Persona("Valeria", 25, 2000)

persona_1.transferencia(persona_2, 4000)
persona_1.mostrar_saldo()
# persona 2
persona_2.mostrar_saldo()
