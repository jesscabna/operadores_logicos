# Los operadores lógicos o logical operators nos permiten trabajar con valores de tipo booleano. Un valor booleano o bool es un tipo que solo puede tomar valores True o False.

stock = int(input('Ingrese el numero de stock: '))
val = stock >= 100and stock <= 1000

if val == True:
  print("Su pedido sera atendido de inmediato")
else: print("Su pedido no cumple con los requeriminetos")

#El operador ‘and’ sirve para realizar condiciones combinadas es decir, por ejemplo : que el numero ingresado sea mayor que ‘100’ pero menor que ‘1000’. Si ambas condiciones se cumplen entonces el operador ‘and’ retornara un ‘True’, si no se cumple un ‘False’. Esto puede ser utilizado en un condicional ‘if;