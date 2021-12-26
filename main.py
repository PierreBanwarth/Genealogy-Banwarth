from meza import io

records = io.read('table1.mdb') # only file path, no file objects
print(next(records))
