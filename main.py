from meza import io

Enregistrements = io.read('table1.mdb') # only file path, no file objects

test = next(Enregistrements)
while test:
    print(test)
