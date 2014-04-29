people = 30
cars = 40
buses = 15

#entra al if por que las personas  son menos que los carros
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

#entra el elif por que como no se cumple el if pasa al if anidado 
#y entra
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

#entra al if  si se cambia la sentencia logica por esta if people < buses: 
#entrara al else ya que no se cumple 
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."