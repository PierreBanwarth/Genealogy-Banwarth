from meza import io

Enregistrements = io.read('table1.mdb') # only file path, no file objects

for x in Enregistrements:
    print(x.decode("utf-16"))
