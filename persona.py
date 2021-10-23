## clase padre
class Persona():
    def __init__(self, id_empleado, dni, nombre, apellido):
        self.id_empleado = id_empleado
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        
    # def __str__(self):
    #     return "DNI {}, Nombre: {}, Apellido {}".format(self.dni, self.nombre, self.apellido)

## clase hija hereda de persona
class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, nro_cliente):
        super().__init__(dni, nombre, apellido)
        self.nro_cliente = nro_cliente
    
    def __str__(self):
        cad = "DNI {}, Nombre: {}, Apellido {}, Numero de cliente {}"
        return cad.format(self.dni, self.nombre, self.apellido, self.nro_cliente)
