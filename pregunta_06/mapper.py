#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    for line in sys.stdin:
       data=line.split(' ')[0]
       num =line.split(" ")[-1]
       sys.stdout.write(data + "\t" + num )