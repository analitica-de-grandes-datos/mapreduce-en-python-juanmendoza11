#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    curkey = None
    val_aux = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == curkey:
            if val > val_aux:
                val_aux = val
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, val_aux))
            curkey = key
            val_aux = val
    sys.stdout.write("{}\t{}\n".format(curkey, val_aux))