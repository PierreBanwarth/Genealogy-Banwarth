import csv, pyodbc
def restore_windows_1252_characters(s):
    """Replace C1 control characters in the Unicode string s by the
    characters at the corresponding code points in Windows-1252,
    where possible.

    """
    import re
    def to_windows_1252(match):
        try:
            return bytes([ord(match.group(0))]).decode('windows-1252')
        except UnicodeDecodeError:
            # No character at the corresponding code point: remove it.
            return ''
    return re.sub(r'[\u0080-\u0099]', to_windows_1252, s)

# set up some constants
MDB= 'C:\\Users\\Pierre\\Documents\\GitHub\\Genealogy-Banwarth\\table1.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'

# connect to db
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Pierre\\Documents\\GitHub\\Genealogy-Banwarth\\table1.mdb')
cursor = conn.cursor()

for table_info in cursor.tables(tableType='TABLE'):
    print(table_info.table_name)

test = cursor.statistics('TABLE1')
for item in test:
    print(item)


cursor.execute("select * from Table1")
row = cursor.fetchone()
i = 0
while row is not None:
    liste = list(row)
    for item in liste:
        print(restore_windows_1252_characters(str(item)))
    row = cursor.fetchone()
    i = i+1
print('nous avons trouve '+str(i)+' elements')
# for item in rows:
#
#     print(str(item).replace('\x00', ''))
#
# cur.execute('select * from TABLE2')
# rows = cur.fetchall()
# for item in rows:
#     print(item)
