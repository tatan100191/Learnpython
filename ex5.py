my_name = 'Jonathan '
my_age = 22 # not a lie
my_height = 1.72 # meters
my_weight = 68 # kgs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %r meters tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

'''
queda como una secuencia y se escribe el arreglo de las variables en la 
misma secuencia aqui como no se cambio la d por la r va tomar los digitos sin decimales. 
'''

print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
