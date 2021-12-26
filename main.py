from meza import io

records = io.read('database.mdb') # only file path, no file objects
print(next(records))
