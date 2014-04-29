from sys import argv

script, user_name = argv
prompt = '> '

print "Hola %s, Yo soy %s script." % (user_name, script)
print "Me gustaria que respondieras unas pocas preguntas."
print "Te gustaria %s?" % user_name
likes = raw_input(prompt)

print "Donde vives %s?" % user_name
lives = raw_input(prompt)

print "Que tipo de computador tienes?"
computer = raw_input(prompt)

print """
Muy bien, dijo que %r le gustaria.
tu vives en %r.  No estoy seguro donde es.
y tu tienes una computadora %r.  Nice.
""" % (likes, lives, computer)