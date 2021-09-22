from PIL import Image
from resizeimage import resizeimage
import os, sys
import glob
from pathlib import Path
import shutil


print("TOOL CONVERT TẤT CẢ ANH TRONG FOLDER HIỆN HỮU VỀ CỠ 2000x2000")
print("CHÚ Ý BACKUP DỮ LIỆU ẢNH TRƯỚC KHI CONVERT")
print("CHỈ CHẠY SCRIPT 1 LẦN CHO 1 FOLDER")
print ("BẤM: \n1. BẮT ĐẦU CONVERT\n2. THOÁT")
var=input("LỰA CHỌN CỦA BẠN:")
if str(var)!='1':  
    exit()
dirs = os.getcwd()
path = os.getcwd()
bk=os.path.join(path,r'pybackup')
Path(bk).mkdir(parents=True, exist_ok=True)


def getallimage(cdir):
    os.chdir(cdir)
    ext = ['*.png', '*.jpg', '*.gif']
    files=[]
    for filee in ext:
        files.extend(glob.glob(filee))
    return files
def resiei(files,p,bkd):
    for f in files:
        pa=os.path.join(p,f)
        Path(bkd).mkdir(parents=True, exist_ok=True)
        bkp=os.path.join(bkd,f)
        
        im = Image.open(pa)
        imResize = resizeimage.resize('thumbnail', im, [1000, 1000])
        im.close()
        shutil.move(pa,bkp)
        imResize.save(f, 'JPEG', quality=90)

p=path
files=getallimage(p)
bkd=bk
resiei(files,p,bkd)
depth = 10
stuff = os.path.abspath(os.path.expanduser(os.path.expandvars(p)))

for root,dirs,files in os.walk(stuff):
    if root[len(stuff):].count(os.sep) < depth:
        for d in dirs :
            pax=(os.path.join(root,d))
            if (bk not in pax) and ("\\lib\\" not in pax):
                xap=pax.replace(p,"")
                xap=xap[1:]
                bkd=os.path.join(bk,xap)
                files=getallimage(pax)
                print(files)
                resiei(files,pax,bkd)
input("ĐÃ HOÀN TẤT. BẤM PHÍM BẤT KỲ ĐỂ THOÁT...")
input("")