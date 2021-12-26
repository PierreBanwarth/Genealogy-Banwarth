from meza import io

Enregistrements = io.read('table1.mdb') # only file path, no file objects

while test = next(Enregistrements):
    print(test)
