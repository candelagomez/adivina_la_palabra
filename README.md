Trabajo Práctico: Juego "Adivina la Palabra"

Descripción del Proyecto
Este proyecto consiste en el desarrollo de un juego de consola en Python, similar al clásico "Ahorcado". El objetivo del Trabajo Práctico es demostrar la comprensión y aplicación de lógica de programación, estructuras de control y manipulación de datos.
El usuario debe descubrir una palabra oculta seleccionada aleatoriamente por el sistema, ingresando letras una por una antes de agotar sus intentos disponibles.

Objetivos y Requerimientos
El desarrollo del software cumple con los siguientes requerimientos funcionales y técnicos solicitados en la consigna:
1. Requerimientos Funcionales
Selección Aleatoria: El sistema debe elegir una palabra al azar de un banco de datos predefinido al iniciar cada partida.
Ocultamiento: La palabra debe mostrarse inicialmente como una serie de guiones bajos (ej: _ _ _ _ _) representando la longitud de la misma.
Sistema de Vidas: El jugador comienza con un número limitado de intentos (vidas). Cada error descuenta una vida.
Interacción: El sistema debe solicitar el ingreso de una letra por turno.
Feedback:
Si el usuario acierta, se debe revelar la letra en su(s) posición(es) correcta(s).
Si el usuario falla, se debe informar el error y el recuento actual de vidas.
Condiciones de Fin:
Victoria: El usuario completa la palabra antes de perder todas las vidas.
Derrota: El contador de vidas llega a cero.

3. Requerimientos Técnicos
Para la resolución del algoritmo se han implementado las siguientes herramientas del lenguaje Python:
Módulo random: Para la selección aleatoria de la palabra secreta.
Listas (list): Estructura fundamental para manejar la "máscara" de la palabra (los guiones que se van reemplazando) y el almacenamiento de letras.
Bucles (Loops):
while: Para mantener el flujo del juego activo mientras queden vidas y la palabra no esté completa.
for: Para recorrer la palabra secreta y verificar las coincidencias de la letra ingresada.
Estructuras Condicionales (if/else): Para la toma de decisiones (acierto vs. error) y validación de fin de juego.
Validación de Datos: Control de entrada para asegurar que el usuario ingrese caracteres alfabéticos válidos y no números o símbolos.
