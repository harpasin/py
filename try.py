f = open('newfile',"wb")
f.seek(31073741824-1)
f.write(b"\0")
f.close()
import os
os.stat("newfile").st_size
