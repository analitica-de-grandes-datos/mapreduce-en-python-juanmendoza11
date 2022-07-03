#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    max=0
    curkey=None
    for line in sys.stdin:
        key=row[0]
        value=int(row[1])
        row=line.split("\t")
        if curkey==key:
            if value>max:
                max=value
            else:
                value=max
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, max))
            curkey=key
            max=value
    sys.stdout.write("{}\t{}\n".format(curkey, max))