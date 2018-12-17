import sys

for line in sys.stdin:
    word = line.split(',')
    latitud = word[4]#recibe la latitud
    longitud = word[3]#recibe la altitud
    aux = word[2].split(' ')
    date = aux[0]
    aux2 = date.split('-')
    year = aux2[0]
    print(latitud + " " + longitud + " " + date + " "+ year)
#python mapper.py < "ave.csv"
