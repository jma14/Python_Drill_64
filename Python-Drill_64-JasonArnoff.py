import os
import shutil
from datetime import *

src = 'C:\Users\Owner\Desktop\Source Folder'
dest = 'C:\Users\Owner\Desktop\Receiving Folder'

currentTime = datetime.now()
twentyFourHoursAgo = currentTime + timedelta(hours=-24)

files = os.listdir(src)

for f in files:
    src_file = src + '\\' + f
    lastModUnix = os.path.getmtime(src_file)
    lastMod = datetime.fromtimestamp(int(lastModUnix))
    if lastMod >= twentyFourHoursAgo:
        dest_file = dest + '\\' + f
        shutil.copy(src_file, dest_file)
