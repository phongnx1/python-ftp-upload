import time
import os.path, os
from ftplib import FTP, error_perm

host = '54.173.216.64'
port = 21

ftp = FTP()
ftp.connect(host,port)
ftp.login('phongnx-ftp','password')
filenameCV = "/Users/phongnx/Main/Learning/Python/upload"

def placeFiles(ftp, path):
    for name in os.listdir(path):
        print(name)
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            # print("STOR", name, localpath)
            ftp.storbinary('STOR ' + name, open(localpath,'rb'))
        elif os.path.isdir(localpath):
            # print("MKD", name)

            # try:
            #     ftp.mkd(name)

            # # ignore "directory already exists"
            # except error_perm as e:
            #     if not e.args[0].startswith('550'): 
            #         raise

            # print("CWD", name)
            # ftp.cwd(name)
            placeFiles(ftp, localpath)
            # print("CWD", "..")
            # ftp.cwd("..")

start_time = time.time()
placeFiles(ftp, filenameCV)
print("--- %s seconds ---" % (time.time() - start_time))

ftp.quit()