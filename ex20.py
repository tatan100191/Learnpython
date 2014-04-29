from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0) #lee desde este caracter

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "imprimimos todo con la primera funcion"

print_all(current_file)

print "se devuleve al caracter numero 0 para que pueda ser leido"

rewind(current_file)

print "lee las lineas por separado"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)