#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys
from collections import OrderedDict
if __name__ == '__main__':
    dicty = {}
    for line in sys.stdin:
       num, letters = line.split('\t')
       num = int(num)
       letters = letters.strip() 
       letters = letters.split(',')
       for x in letters:
         if x in dicty.keys():
           dicty[x].append(num)
         else:
           dicty[x] = [num]
    for ky in sorted(dicty.keys()):
      nums = sorted(dicty[ky])
      final_nums = ",".join([str(value) for value in nums])
      sys.stdout.write("{}\t{}\n".format(ky,final_nums))