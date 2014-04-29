def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "nosotros podemos ingresar directamente los numeros:"
cheese_and_crackers(20, 30)


print "o, podemos generar las variables y enviarlas como parametros"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "podemos utilizar formulas matematicas en lo parametros"
cheese_and_crackers(10 + 20, 5 + 6)


print "y podemos combinar las dos, variables y formulas matematicas"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)