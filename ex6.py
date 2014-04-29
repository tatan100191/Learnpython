x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
#cuando la variables es una cadena la %r le coloca comillas
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# une las dos cadenas
print w + e