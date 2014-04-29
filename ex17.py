from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# abre el archivo que sera copiado y lo lee
in_file = open(from_file)
indata = in_file.read()
print indata
print "The input file is %d bytes long" % len(indata)#tamano del archivo

print "Does the output file exist? %r" % exists(to_file)# mira si el archivo existe
print "Ready, hit INTRO to continue, CTRL-C to abort."
raw_input()

# Abre el archivo en modo escritura y lo escribe
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()

in_file.close()