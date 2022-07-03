#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

# Clave - valor

import sys
if __name__ == "__main__":
  for line in sys.stdin:
    col = line.split(',')
    col_credit_history = col[2]
    sys.stdout.write("{}\t1\n".format(col_credit_history))