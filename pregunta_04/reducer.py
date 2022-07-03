#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys
if __name__ == '__main__':
    total = 0
    curkey = None
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == curkey:
            total += val
        else:
            if curkey is not None:
                sys.stdout.write("{},{}\n".format(curkey, total))
            curkey = key
            total = val
    sys.stdout.write("{},{}\n".format(curkey, total))