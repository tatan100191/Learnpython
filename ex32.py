the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# el primer tipo de bucle for  es mediante una lista
for number in the_count:
    print "This is count %d" % number

# igual que el anterior
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# tambien lo podemos hacer con una lista mixta
# se usa %r para cual tipo de dato
for i in change:
    print "I got %r" % i

# con un bucle podemos generar u lista desde cero
elements = []

#  entonces el rango que se utiliza es de 0 a 5
#  se observa que el range funciona tomando el 0 pero no el 6
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append es un metodo para agregar al final de la lista 
    elements.append(i)
    # esto imprime todo el arreglo -> print elements

# ahora imprimimos de la misma forma que en los primeros bucles
for i in elements:
    print "Element was: %d" % i