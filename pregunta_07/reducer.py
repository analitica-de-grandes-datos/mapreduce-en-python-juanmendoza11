#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
 campo_lista=[]
 for line in sys.stdin:
    marca, date, value = line.split("\t") 
    value=int(value) 
    campo_lista.append([marca, date, value]) 
 campo_lista = sorted(campo_lista, key=lambda x: (x[0], x[2])) 
 for line in campo_lista: 
    sys.stdout.write(line[0] +"   " + line[1] +"   " + str(line[2]) + "\n")