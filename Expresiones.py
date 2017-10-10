import re

Cadena =raw_input("Ingrese la operacion en posorden: ")
lista = cadena.split(" ")
patronVariables = re.compile('[A-Z]', re.I)
patronValores = re.compile('[0-9]')
patronSignos = re.compile('[+*/=-]')

listaErrores1 = [x for x in lista if x not in patronVariables.findall(cadena)]
listaErrores2 = [x for x in listaErrores1 if x not in patronValores.findall(cadena)]
listaErroresFinal = [x for x in listaErrores2 if x not in patronSignos.findall(cadena)]

if len(listaErroresFinal)==0:
    print "No hay errores."
else:
    print "Errores existentes: "
    print len(listaErroresFinal)
    print listaErroresFinal
    print "\n\n\n"
    
cadenaSalida = ""

for i in range (len(lista)):
    if not(patronVariables.search(lista[i]) is None):
        cadenaSalida = cadenaSalida + "("+lista[i]+",VARIABLE)\n"

    elif not(patronValores.search(lista[i]) is None):
        cadenaSalida = cadenaSalida + "("+lista[i]+",VALOR)\n"
        
    elif not(patronSignos.search(lista[i]) is None):
        cadenaSalida = cadenaSalida + "("+lista[i]+",SIGNO)\n"

    else:
        cadenaSalida = cadenaSalida + "("+lista[i]+",ERROR)\n"

print cadenaSalida
