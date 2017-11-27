import numpy as np
import re
import sys


data = np.genfromtxt(str(sys.argv[1]), unpack=True)

def columnsettings(a):
    lengthnv = 0
    lnv = 0
    lengthnn = 0
    lnn = 0
    lenghtu = 0
    lu = 0
    lenghte = 0
    le = 0

    num = re.compile(r"^-{0,1}\d+(.\d+(\\pm\d+(.\d+){0,1}(e\(-{0,1}\d+\)){0,1}){0,1}){0,1}$")
    k = re.compile(r".")
    nv = re.compile(r"(?=^-{0,1})\d+")
    nn = re.compile(r"(?=^-{0,1}\d+.)\d+")
    u = re.compile(r"(?=^-{0,1}\d+(.\d+){0,1}\\pm)\d+(.\d+){0,1}")
    e = re.compile(r"(?=^-{0,1}\d+(.\d+(\\pm\d+(.\d+){0,1}){0,1}){0,1}e)\d+")
#    e = re.compile(r"(?=^-{0,1}\d+(.\d+(\\pm\d+(.\d+){0,1}e\()-{0,1}\d+")

    for i in a:
        if not num.match(str(i)):
            return "c"
        a = nv.match(str(i))
        lengthnv = len(a.group()) if a else 0
        a = nn.match(str(i))
        lengthnn = len(a.group()) if a else 0
        b = u.match(str(i))
        lengthu = len(b.group()) if b else 0
        a = e.match(str(i))
        lengthe = len(a.group()) if a else 0
        if(b):
            if(k.match(b.group())): lengthu -= 1
        if(lengthnv > lnv): lnv = lengthnv
        if(lengthnn > lnn): lnn = lengthnn
        if(lengthu > lu): lu = lengthu
        if(lengthe > le): le = lengthe
    return "S[table-format=" + str(lnv) + "." + str(lnn-1) + "(" + str(lu) + ")e" + str(le) + "]"


print("\\begin{table}")
print("\t\\centering")
print("\t\\caption{.}")
print("\t\\begin{tabular}{", end="")
for i in data:
    print(columnsettings(i), end=" ")
print("}")
print("\t\t\\toprule")

file = open(str(sys.argv[1]), "r")
kopfzeile = file.readline()
file.close()
kopfzeile = [x.strip() for x in kopfzeile.split(',')]
kopfzeile = [x.strip("#") for x in kopfzeile]

for i in range(len(kopfzeile) -1):
    print("\t\t{$", kopfzeile[i], "$} & ", end="", sep="")
print("\t\t{$", kopfzeile[-1], "$} \\\\", sep="")

print("\t\t\\midrule")

for j in range(data[0].size):
    print("\t\t", end="")
    for i in range(int(round(data.size/data[0].size)) -1):
        print(data[i][j], "\t& ", end="", sep="")
    print(data[-1][j], "\t\\\\")

print("\t\t\\bottomrule")
print("\t\\end{tabular}")
print("\\end{table}")

