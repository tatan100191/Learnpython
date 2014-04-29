i = 0
numbers = []
#mientras i sea < a 6 va agregar al arreglo el valor de i
# osea que va llenar desde 0 a 5
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num