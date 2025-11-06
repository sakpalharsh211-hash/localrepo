import sys
import os
def read_lastnlines(sample,lines):
    bufsize=8192
    fsize=os.stat(sample).st_size
    iter=0
    with open(sample) as f:
        if bufsize > fsize:
            bufsize=fsize-1
            data=[]
            while True:
                iter+=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell()==0:
                    print(''.join(data[-lines:]))
                    break
read_lastnlines('sample.txt',2)
