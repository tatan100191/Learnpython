from sys import argv

script, filename = argv

txt = open(filename)#abre el archivo

print "Here's your file %r:" % filename
print txt.read()#lee el archivo

print "Type the filename again:"
file_again = raw_input("> ")#guarda la direccion del archivo

txt_again = open(file_again)

print txt_again.read()