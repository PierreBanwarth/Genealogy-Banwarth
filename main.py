from meza import io

Enregistrements = io.read('table1.mdb') # only file path, no file objects

for x in Enregistrements:
    with open(x, encoding="utf-16") as f:
        print(x)
