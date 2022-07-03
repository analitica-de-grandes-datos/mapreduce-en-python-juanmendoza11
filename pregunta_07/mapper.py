#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":
 for line in sys.stdin:
           letter = line.split('   ')[0]
           date = line.split('   ')[1]
           number = int(line.split('   ')[2])
           sys.stdout.write("{}\t{}\t{}\n".format(letter,date,number))