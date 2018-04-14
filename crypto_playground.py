# Solving challenge here

from crypto_tools.substitute import *
from crypto_tools.analysis import *

lines = """tm bcsv qolfp
f'dmvd xuhm exl tgak
hlrkiv sydg hxm
qiswzzwf qrf oqdueqe
dpae resd wndo
liva bu vgtokx sjzk
hmb rqch fqwbg
fmmft seront sntsdr pmsecq""".split("\n")

for line in lines:
    print("SOLVING LINE : {} ".format(line))
    for solve in brute_force(line):
        print(solve)
    print("_"*100)
