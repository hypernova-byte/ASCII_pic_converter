from PIL import Image
import numpy as np
import os 
import datetime

picture = input("photo name: ") + ".jpeg"
name = ""
for i in range(len(picture)-4):
    name += picture[i]
im = Image.open(picture, "r")
WIDTH, HEIGHT = im.size
pix_val = list(im.getdata())
pix_val = np.array(pix_val).reshape((WIDTH, HEIGHT, 3))
bright = []
time = datetime.datetime.now()
tag = time.strftime("%M%S")

revert = input("invert colour? yes/no: ")
if revert.upper() == "YES":
    revert = True
else:
    revert = False

spacing = input("space between ASCII letters? yes/no: ")
if spacing.upper() == "YES":
    spacing = True
else:
    spacing = False

contrast = input("contrast level (2 is normal): ")
try:
    contrast = int(contrast)
except:
    contrast = 2
charstring = "N@#W$9876543210?!abc;:+=-,._"
charstring += (contrast * " ")
chars = [x for x in charstring]

def luminescence(r, g, b):
    return (r + g + b) / 3

def pxl_char(n):
    if revert == False:
        return round((n-5)/255 * 28) + 1
    else:
        return round ((n-5)/255 * 28)

def main():

    for i in pix_val:
        for j in i:
            bright.append(luminescence(j[0], j[1], j[2]))
    bright_np = np.array(bright).reshape(HEIGHT, WIDTH)
    pic = ""
    if revert == False:
        for i in bright_np:
            for j in i:
                pic += chars[-pxl_char(j)]
                if spacing:
                    pic += " "
            pic += "\n"
    else:
        for i in bright_np:
            for j in i:
                pic += chars[pxl_char(j)]
                if spacing:
                    pic += " "
            pic += "\n"
    #only works on macos + needs folder named output_pics in current directory
    os.chdir("output_pics")
    os.system(f"touch {name}{tag}.txt & echo '{pic}' >> {name}{tag}.txt")

if __name__ == "__main__":
    main()