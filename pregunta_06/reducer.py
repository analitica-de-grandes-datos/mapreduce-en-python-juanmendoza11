#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys
if __name__ == '__main__':
    curkey = None
    valor_maximo = 0
    valor_minimo = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = float(val)
        if key == curkey:
            if (val> valor_maximo):
                valor_maximo=val
            if (val< valor_minimo):
                valor_minimo=val
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, valor_maximo,valor_minimo))
            curkey = key
            valor_maximo = val
            valor_minimo = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, valor_maximo, valor_minimo))