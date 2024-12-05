from proceso import Proceso

# Crear los procesos
Proceso_Cero = Proceso("Proceso_Cero", 0)
Proceso_Uno = Proceso("Proceso_Uno", 1)

# Lista donde se van guardando los resultados
salida = []

def alternar_procesos():
    """
        Alterna el estado de los procesos `Proceso_Cero` y `Proceso_Uno`.

        Este método invierte el estado de ambos procesos (`Proceso_Cero` y `Proceso_Uno`) llamando a su
        método `cambiar()`, que alterna el valor de su estado (de `0` a `1` o de `1` a `0`).

        Lógica:
            - Se invierte el estado del proceso `Proceso_Cero`.
            - Se invierte el estado del proceso `Proceso_Uno`.

        Este método permite realizar una alternancia de estados entre dos procesos, lo cual puede ser útil
        para sincronizar o controlar el flujo de los procesos según su estado.

        Example:
            # Antes de llamar a alternar_procesos
            print(Proceso_Cero.getEstado())  # Imprime: 0
            print(Proceso_Uno.getEstado())   # Imprime: 1

            alternar_procesos()

            # Después de llamar a alternar_procesos
            print(Proceso_Cero.getEstado())  # Imprime: 1
            print(Proceso_Uno.getEstado())   # Imprime: 0
        """


def procesar(proceso_x: Proceso):
    """
    Procesa un objeto de tipo `Proceso` y actualiza la lista `salida` según el estado del proceso.

    Este método evalúa el estado del objeto `proceso_x`. Si el estado del proceso es `1`, agrega `1` a la lista `salida`;
    de lo contrario, agrega `0`. Luego, llama al método `prosesar()` del objeto `proceso_x` para realizar alguna operación
    relacionada con el proceso.

    Args:
        proceso_x (Proceso): Un objeto de la clase `Proceso` que contiene un estado y un contador.

    Lógica:
        - Se verifica el estado de `proceso_x`. Si es `1`, se agrega `1` a la lista `salida`.
        - Si el estado de `proceso_x` es `0`, se agrega `0` a la lista `salida`.
        - Después de la evaluación del estado, se llama al método `prosesar()` del objeto para continuar con su procesamiento.

    Variables:
        salida (list): Lista global donde se agregan valores dependiendo del estado del proceso.
        proceso_x.estado (int): El estado del proceso, utilizado para determinar qué valor agregar a `salida`.

    Example:
        proceso = Proceso("Proceso_A", 0)
        procesar(proceso)

        # Si el estado del proceso es 0, se agrega 0 a la lista `salida`.
        print(salida)  # Imprime: [0]

        # Si se cambia el estado del proceso y se llama de nuevo:
        proceso.estado = 1
        procesar(proceso)

        print(salida)  # Imprime: [0, 1]
    """
    salida.append(1 if proceso_x.estado==1 else 0)
    proceso_x.prosesar()

# Inicia en 1 la salida : se procesa el proceso 1 primero
procesar(Proceso_Uno)
def sincronizar():
    """
        Sincroniza el proceso según los valores de la lista `salida`.

        Este método recorre la lista `salida` y compara el valor de cada elemento con su anterior para
        decidir qué proceso ejecutar (`Proceso_Uno` o `Proceso_Cero`). Si el valor anterior es `0`,
        se llama a `procesar(Proceso_Uno)`, y si es diferente (en este caso se asume que es `1`),
        se llama a `procesar(Proceso_Cero)`.

        El proceso sigue los siguientes pasos para cada elemento:
        - Recorre la lista `salida` de forma secuencial.
        - Compara el valor actual con el valor anterior.
        - Ejecuta el proceso correspondiente (`Proceso_Uno` o `Proceso_Cero`) dependiendo del valor comparado.

        Variables:
            salida (list): Lista que contiene los valores a comparar. La longitud de la lista dicta
                           cuántas veces se ejecutará el ciclo.
            anterior (int): Almacena el valor del elemento anterior en la lista `salida`.
            actual (int): Almacena el valor del elemento actual en la lista `salida`.

        Lógica:
            - Para cada elemento en la lista `salida`, se compara su valor con el anterior.
            - Si el valor anterior es `0`, se ejecuta `procesar(Proceso_Uno)`.
            - Si el valor anterior es distinto de `0`, se ejecuta `procesar(Proceso_Cero)`.

        Example:
            salida = [0, 1, 0, 1]
            sincronizar()

            # Durante la ejecución:
            # 1. Compara el primer y segundo elemento, ejecutando 'procesar(Proceso_Cero)'.
            # 2. Compara el segundo y tercer elemento, ejecutando 'procesar(Proceso_Uno)'.
            # 3. Repite para el resto de los elementos de la lista.
        """
    for i in range(1, len(salida)+1):
        anterior = salida[i - 1]
        actual = salida[i-1]

    if anterior == 0:
        procesar(Proceso_Uno)
    else: procesar(Proceso_Cero)

# Proceso Principal main
while len(salida) < 200:
    sincronizar()


# Imprimir el resumen
print("\n--- Resumen de Procesos ---")
print(f"Proceso: {Proceso_Cero.nombre} | Contador: {Proceso_Cero.contador}")
print(f"Proceso: {Proceso_Uno.nombre} | Contador: {Proceso_Uno.contador}")

# imprimir como caracteres, en una línea y sin espacios los n elementos de la lista
print("\n--- Salida ---")
print("".join(map(str, salida)))

