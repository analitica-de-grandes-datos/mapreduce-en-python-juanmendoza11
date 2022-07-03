#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        data = line.split()[1]
        month = data.split("-")[1]
        sys.stdout.write("{}\t1\n".format(month))