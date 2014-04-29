people = 20
cats = 30
dogs = 15

#como el valor de las personas es menor que el de los gatos entra al if e imprime
if people < cats:
    print "Too many cats! The world is doomed!"

#como el valor de las personas es menor que el de los gatos no entra al if
if people > cats:
    print "Not many cats! The world is saved!"

#como el valor de las personas es mayor al de los perros no entra al if
if people < dogs:
    print "The world is drooled on!"

#como el valor de las personas es mayor que la de los perros entra al if e imprime
if people > dogs:
    print "The world is dry!"


dogs += 5
# entra al if por que los perros y las personas tienen el mismo valor
if people >= dogs:
    print "People are greater than or equal to dogs."

# entra al if por que los perros y las personas tienen el mismo valor
if people <= dogs:
    print "People are less than or equal to dogs."

# entra al if por que los perros y las personas tienen el mismo valor
if people == dogs:
    print "People are dogs."