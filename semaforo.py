class Semaforo:
    """
    Clase que implementa un semáforo binario con estados 0 y 1.

    La clase permite crear semáforos que pueden alternar entre dos estados (0 y 1),
    útil para la sincronización de procesos.

    Attributes:
        estado (int): Estado actual del semáforo (0 o 1)

    Example:
        # Crear dos semáforos con estados iniciales diferentes
        Proceso_A = Semaforo(0)
        Proceso_B = Semaforo(1)

        # Obtener estados iniciales
        print(Proceso_A.getEstado())  # Imprime: 0
        print(Proceso_B.getEstado())  # Imprime: 1

        # Cambiar estado de cada semáforo
        Proceso_A.cambiar()  # Cambia a 1
        Proceso_B.cambiar()  # Cambia a 0

        # Verificar nuevos estados
        print(Proceso_A.getEstado())  # Imprime: 1
        print(Proceso_B.getEstado())  # Imprime: 0
    """

    def __init__(self, estado_inicial):
        """
        Inicializa un nuevo semáforo con el estado especificado.

        Args:
            estado_inicial (int): Estado inicial del semáforo (0 o 1)

        Raises:
            ValueError: Si el estado_inicial no es 0 o 1
        """
        if estado_inicial not in [0, 1]:
            raise ValueError("El estado debe ser 0 o 1")
        self.estado = estado_inicial

    def cambiar(self):
        """
        Cambia el estado del semáforo.

        Si el estado actual es 0, cambia a 1.
        Si el estado actual es 1, cambia a 0.
        """
        self.estado = 0 if self.estado == 1 else 1

    def getEstado(self):
        """
        Obtiene el estado actual del semáforo.

        Returns:
            int: Estado actual del semáforo (0 o 1)
        """
        return self.estado