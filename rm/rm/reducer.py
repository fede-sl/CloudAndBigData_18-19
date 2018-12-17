import sys

if len(sys.argv) <= 1:
    exit(0)
nombreArchivo = sys.argv[1]
f=open("output/" + nombreArchivo, "w")
for line in sys.stdin:
	f.write(line.replace(" ", ",") + "\n")
	
f.close()
#python mapper.py < "ave.csv" | sort | python reducer.py
	
