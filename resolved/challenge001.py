# Résolution du challenge chiffrement par décalage
# Lien : https://www.root-me.org/fr/Challenges/Cryptanalyse/Substitution-monoalphabetique-Cesar

# Import crypto tools
from crypto_tools.substitute import *
from crypto_tools.analysis import *

message =  """tm bcsv qolfp
f'dmvd xuhm exl tgak
hlrkiv sydg hxm
qiswzzwf qrf oqdueqe
dpae resd wndo
liva bu vgtokx sjzk
hmb rqch fqwbg
fmmft seront sntsdr pmsecq"""

for line in message.split("\n"):
    print("SOLVING LINE : {}".format(line))
    for solve in brute_force(line):
        print(solve)
    print("_"*100)
