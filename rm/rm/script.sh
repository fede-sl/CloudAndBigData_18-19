#/bin/bash

FILES=datasheets/*

for file in $FILES
do 
    echo "Este archivo es: $file"
    python mapper.py < "$file" | python reducer.py "$(basename $file)"
done
