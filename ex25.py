def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')# divede la cadena cada vez que encuetra un espacio
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)# devuelve el arreglo desordenado pero 
                        #siempre es el mismo arreglo desordenado

def print_first_word(words): 
    """Prints the first word after popping it off."""
    word = words.pop(0)# saca el primer valor del arreglo
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)#saca el ultimo valor del arreglo
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)# llama la primera funcion que divide la sentencia
    return sort_words(words)#y el arreglo que devuelve lo manda como parametro a la que los desordena
                            #y devulve el resultado

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)# hace el arreglo
    print_first_word(words)# imprime el primer valor
    print_last_word(words)# imprime el ultimo valor 

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# sentencias 
"""
tatan@tatan:~/mystuff$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import ex25
>>> sentencia = "aqui va lo que desea escribir"
>>> palabras = ex25.break_words(sentencia)
>>> palabras
['aqui', 'va', 'lo', 'que', 'desea', 'escribir']
>>> palabras_azar = ex25.sort_words(palabras)
>>> palabras_azar
['aqui', 'desea', 'escribir', 'lo', 'que', 'va']
>>> ex25.print_first_word(palabras)
aqui
>>> ex25.print_last_word(palabras)
escribir
>>> palabras
['va', 'lo', 'que', 'desea']
>>> ex25.print_first_word(palabras)
va
>>> ex25.print_last_word(palabras)
desea
>>> palabras_azar
['aqui', 'desea', 'escribir', 'lo', 'que', 'va']
>>> palabras_azar = ex25.sort_sentence(sentencia)
>>> palabras_azar
['aqui', 'desea', 'escribir', 'lo', 'que', 'va']
>>> ex25.print_first_and_last(sentencia)# pero en este caso no se pierden 
                            # los valores por que actua en el arreglo que se define 
                            # en la consola
aqui
escribir
>>> ex25.print_first_and_last_sorted(sentencia)
aqui
va
"""
