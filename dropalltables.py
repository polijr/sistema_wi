import os
from os import walk


    #   _________      ___    ___    __________     _____        _________
    #  /.....____|    |..|   |..|   |...___...|     |...|     /....._____|
    # /...../         |..|___|..|   |../   \..|     |...|     |..../
    # |..../          |.._____..|   |..\___/../     |...|      \__ .\
    # |.../           |..|   |..|   |...__.../      |...|         \_..\
    # \....\          |..|   |..|   |..|   \..\     |...|           |...\
    #  \.....\        |..|   |..|   |..|    \..\    |...|           |...|
    #   \.....\____   |..|   |..|   |..|     \..\   |...|      ____/..../
    #    \________|   |__|   |__|   |__|      \__\  |___|      |_______/

##################################
	# Made by: Chris Hukai
	# christian.hukai@gmail.com
	# ~~ nTec rules ~~
##################################


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
