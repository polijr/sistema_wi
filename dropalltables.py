import os
from os import walk


dir = str(os.path.dirname(os.path.abspath(__file__)))
for (dirpath, dirnames, filenames) in walk(dir):
    for x in filenames:
        if x.startswith("00") or x.startswith("db.sqlite3"):
            try:
                os.remove(os.path.join(dirpath, x))
            except:
                pass

print('==========================')
print('Todas migrations deletadas')
print('==========================')
