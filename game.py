"""
          Juego matematico

Consiste en tratar de resolver 5 operaciones aleatorias (+,-,*,/) con el
objetivo de lograr la mayor cantidad de puntos en el  menor tiempo posible.

- Maximo de puntos posibles: (5)
- Resultado incorrecto: no resta puntos
- Puntos por operacion: (1)

"""

from random import choice, randrange
from datetime import datetime

def operacion(num1 , num2 , op):     #proceso que realiza todas las operaciones
    if (op == "+"):
        return (num1 + num2)
    elif (op == "-"):
        return(num1 - num2)
    elif (op == "/"):
        try:
            resultadoTemp = num1 / num2
        except ZeroDivisionError:
            return 0
        return (num1 // num2)
    else:
        return (num1 * num2)            

operators = ["+", "-","/","*"]         # Operadores posibles
times = 5                              # Cantidad de cuentas a resolver
puntos = 0                             #Contador de puntos
init_time = datetime.now()             # Contador inicial de tiempo. Esto toma la fecha y hora actual.
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):              # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    r = operacion(number_1, number_2, operator)
    result = input("Resultado: ")
    while not result.isnumeric():
        print('Ingresar un entero')
        result = input("resultado: ")
    if(int(result) == r):
        print("El resultado es correcto")
        puntos += 1
    else:
        print("El resultado es incorrecto")

end_time = datetime.now()
total_time = end_time - init_time      # Restando las fechas obtenemos el tiempo transcurrido.
print(f"\n Tardaste {total_time.seconds} segundos.")  # Mostramos ese tiempo en segundos.
print(f"\n Tus puntos logrados fueron: {puntos}")