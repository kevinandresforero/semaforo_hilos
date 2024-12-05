# Simulador de Semáforo y Hilos de Procesos en un Computador

Este repositorio contiene un simulador que modela un semáforo binario y su relación con los hilos de procesos en un computador. La idea es representar cómo los procesos se sincronizan y alternan en función del estado del semáforo, lo que refleja cómo los hilos de un sistema operativo pueden ser gestionados para evitar condiciones de carrera y garantizar la ejecución ordenada de tareas.

## Descripción

El proyecto implementa una simulación de un semáforo binario utilizando clases en Python. A través de la clase `Semaforo` y su herencia en la clase `Proceso`, se simulan los procesos que dependen de un semáforo para ejecutar ciertas acciones. Se alternan entre dos estados, `0` y `1`, simulando la sincronización y el control de los hilos en un entorno computacional.

### Características del proyecto

- **Semáforo Binario**: Se utiliza para controlar el acceso a los recursos compartidos entre los procesos, simulando cómo se gestionan los hilos en un sistema operativo.
- **Procesos Sincronizados**: Los procesos se alternan entre dos estados (por ejemplo, `Proceso_Cero` y `Proceso_Uno`), donde cada uno puede estar bloqueado o listo para ejecutarse según el estado del semáforo.
- **Control de Estado de los Procesos**: Los procesos cambian su estado a través de métodos que simulan la manipulación de hilos en un sistema real.
- **Bucle Principal**: El proceso principal sigue ejecutando hasta que se cumple una condición específica, y los procesos se sincronizan y alternan constantemente.

## Estructura del Código

El código está estructurado en las siguientes clases y métodos principales:

1. **Clase `Semaforo`**: Representa el semáforo binario, con métodos para cambiar su estado.
2. **Clase `Proceso`**: Hereda de `Semaforo` y representa un proceso que puede estar en uno de dos estados. Se incluyen métodos para cambiar el estado del proceso y realizar acciones basadas en ese estado.
3. **Métodos de Sincronización y Procesamiento**:
   - `sincronizar()`: Método que sincroniza los procesos según el estado actual del semáforo.
   - `procesar()`: Método que gestiona la ejecución de cada proceso, añadiendo resultados a la lista `salida`.
   - `alternar_procesos()`: Alterna el estado de los procesos `Proceso_Cero` y `Proceso_Uno`.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tuusuario/simulador-semaforo-hilos.git

2. Entra a la carpeta
   ```bash
   cd simulador-semaforo-hilos

3. Opcional
   Activa el entorno virtual
  ```bash
  python -m venv venv
  source venv/bin/activate  # En Linux/Mac
  venv\Scripts\activate     # En Windows
