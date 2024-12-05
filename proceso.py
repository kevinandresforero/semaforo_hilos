from semaforo import Semaforo

class Proceso(Semaforo):
    """
       Clase que representa un proceso con un nombre y hereda las funcionalidades
       de un semáforo binario.

       Attributes:
           nombre (str): Nombre identificativo del proceso.
           estado (int): Estado heredado del semáforo (0 o 1).
           contador (int): Contador interno para rastrear el número de operaciones realizadas.

       Methods:
           __init__(nombre, estado_inicial):
               Inicializa el proceso con un nombre y un estado inicial.
           getNombre():
               Retorna el nombre del proceso.
           setNombre(nuevo_nombre):
               Modifica el nombre del proceso.
           cambiar():
               Cambia el estado actual del semáforo (0 a 1 o 1 a 0).
           procesar():
               Incrementa el contador hasta un máximo de 100. Lanza un error si se supera el límite.

       Example:
           # Crear un proceso
           proceso1 = Proceso("Proceso_A", 0)

           # Obtener nombre y estado
           print(proceso1.getNombre())  # Imprime: Proceso_A
           print(proceso1.getEstado())  # Imprime: 0

           # Cambiar estado
           proceso1.cambiar()
           print(proceso1.getEstado())  # Imprime: 1

           # Procesar valores
           for _ in range(100):
               proceso1.procesar()

           # Intentar procesar más de 100 valores
           try:
               proceso1.procesar()
           except ValueError as e:
               print(e)  # Imprime: "La función procesar solo puede generar 100 valores"
       """

    def __init__(self, nombre, estado_inicial):
        """
        Inicializa un nuevo proceso con nombre y estado inicial.

        Args:
            nombre (str): Nombre del proceso
            estado_inicial (int): Estado inicial del semáforo (0 o 1)
        """
        # Llamamos al constructor de la clase padre (Semaforo)
        super().__init__(estado_inicial)
        # Agregamos el nuevo atributo
        self.nombre = nombre
        self.contador = 0

    def getNombre(self):
        """
        Obtiene el nombre del proceso.

        Returns:
            str: Nombre del proceso
        """
        return self.nombre

    def setNombre(self, nuevo_nombre):
        """
        Modifica el nombre del proceso.

        Args:
            nuevo_nombre (str): Nuevo nombre para el proceso
        """
        self.nombre = nuevo_nombre

    def prosesar(self):
        """
           Incrementa el contador del proceso hasta un máximo de 100.

           Este método se utiliza para realizar un seguimiento del número de operaciones o
           valores procesados por el objeto. Cada vez que se llama al método, el contador se
           incrementa en 1, siempre y cuando no haya superado el límite de 100.

           Si el contador ya ha alcanzado el límite, se lanza una excepción `ValueError`.

           Raises:
               ValueError: Si el contador supera el límite de 100.

           Example:
               proceso = Proceso("Proceso_A", 0)

               # Incrementar el contador
               for _ in range(100):
                   proceso.procesar()

               # Intentar procesar más de 100 valores
               try:
                   proceso.procesar()  # Esto generará un ValueError
               except ValueError as e:
                   print(e)  # Imprime: "La función procesar solo puede usarse 100 valores"
           """
        if self.contador <= 100:
            self.contador = self.contador + 1
        else:
            raise ValueError("La función procesar solo puede usarse 100 valores")