import os, time
import PIL
from PIL import Image
from shutil import copyfile
from stat import *
import datetime

print("CHRIS FRATER's IMAGE HANDLING LIBRARY!  Version 000.01 9-24-2016")
print("E-mail me at: chrisfrater@gmail.com")
print("Stardate: ", datetime.datetime.now())
print("***************")
startingplace = os.getcwd()
whereimagesat = os.path.normpath(r'D:/Dev/Sik/WinTests.sikuli/')
whereimagesgo = os.path.normpath(r"D:/Dev/Sik/CAPTURES/Tests/")
defaultdir = os.path.normpath(r'C:/Users/Chris/Pictures/ImageMakr/')
ezdate = str(datetime.date.today())

print(" Starting Directory: ", os.getcwd())
print("  Project Directory: ", whereimagesat)
print("   Target Directory: ", whereimagesgo)
print("easy date prefix for new folders will be: ", ezdate)
print("***Default Single Image Save Directory: ", defaultdir, " ****")
print("***************")

def CF_single_image(imagefiletoworkwith, wheretosaveto = defaultdir):
    imm = imagefiletoworkwith
    head, tail = os.path.split(imm)         
    print("image is.. ", imm)
    import imghdr
    print(imghdr.what(imm))
    ##MAKEFOLDER TO SAVE IMAGES TO
    new_holder_folder = os.path.join(wheretosaveto, ezdate)
    if not os.path.exists(new_holder_folder):
        os.makedirs(new_holder_folder)
        print("New Holder Folder made at, ", new_holder_folder)
        wheretosaveto = new_holder_folder
    else:
        print("New Holder Folder already exists!  Adding number at the end")
        z = 1
        while (z < 10):
            zzz = "copy_" + str(z)
            print("Trying with ", zzz, " postfix") 
            nnn = os.path.join(new_holder_folder, ezdate + zzz)
            if not os.path.exists(nnn):
                os.makedirs(nnn)
                #print("New Holder Folder made at, ", nnn)
                new_holder_folder = nnn
                z += 10
            z += 1 
    print("Main Target Directory for copies is:", new_holder_folder)
    ##MAKE IMAGE
    im = Image.open(imm)
    ##DIAGNOSTICS
    height = im.height.real
    width = im.width.real
    print("Image Height(real): ", height)
    print("Image Width(real): ", width)
    img_size = im.size
    print("image size(as tuple): %s" % (img_size,))
    st = os.stat(imm)       
    print("ST SIZE REAL (BITESIZE): ", st[ST_SIZE.real])
    ##THUMBNAIL
    print("Converting to Thumbnail")
    nsize = ()
    nsize = (round(img_size[0]/2, 0), round(img_size[1]/2, 0))
    print("New size ", nsize)
    thumbim = im.copy()    
    thumbim.thumbnail(nsize)
    stry = os.path.join(new_holder_folder, "_thumb_" + tail)
    nname = os.path.join(stry)
    print("new nname", nname) 
    nname = os.path.normpath(nname)
    thumbim.save(nname)
    ##CLOSE AND CLEANUP
    thumbim.close() 
    im.close()




def batch_makr(dirofimages, targetdirofcopies, options = "none"):
    print("*****batch_makr Started*****")
    print("")
    os.chdir(dirofimages)
    print("Navigated to image directory, ", dirofimages)
    print("Attempting to make directory at designated target location")
    ###MAKING DIR AT TARGET LOCATON, ASSIGNING THIS TO TARGETDIROFCOPIES
    new_holder_folder = os.path.join(targetdirofcopies, ezdate)
    if not os.path.exists(new_holder_folder):
        os.makedirs(new_holder_folder)
        print("New Holder Folder made at, ", new_holder_folder)
        targetdirofcopies = new_holder_folder
    else:
        print("New Holder Folder already exists!  Adding number at the end")
        z = 1
        while (z < 10):
            zzz = "copy_" + str(z)
            print("Trying with ", zzz, " postfix") 
            nnn = os.path.join(targetdirofcopies, ezdate + zzz)
            if not os.path.exists(nnn):
                os.makedirs(nnn)
                #print("New Holder Folder made at, ", nnn)
                targetdirofcopies = nnn
                z += 10
            z += 1  
    print("Main Target Directory for copies is:", targetdirofcopies)
    ###SETTING UP FOLDERS FOR INDIVIDUAL OPTIONS###
    thumbgo = False
    moreinfo = False
    print("Options called... ")
    if options != "none":
        if options == "t" or "all" or "thumb" or "a":
            thumbgo = True
            print("Thumbnail option called! making thumbnail directory")
            thumbpath = os.path.join(targetdirofcopies, "Thumbnails")
            if not os.path.exists(thumbpath):
                os.makedirs(thumbpath)
                print("Thumbnail folder made at, ", thumbpath)
            else:
                print("Thumbnail path already exists!  Error!")
                exit()
        if options == "i" or "info" or "extensive" or "a":
            moreinfo = True
    else:
        print("No options called, bummer!")     
    i = 0
    print("")
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)    
        if (f_ext == ".PNG") or (f_ext == '.png'):
            cents = ("*******Image number: " + str(i) + " " + f + " STARTED!*********")
            print(cents.center(75))
            print("Opening  ", f, " with Image Library...")
            im = Image.open(f)
            z = im.info.copy()
            print("Image Info: ", z)
            height = im.height.real
            width = im.width.real
            print("Image Height(real): ", height)
            print("Image Width(real): ", width)
            img_size = im.size
            print("image size(as tuple): %s" % (img_size,))
            st = os.stat(f)       
            print("ST SIZE REAL (BITESIZE): ", st[ST_SIZE.real])
            print("Last Accessed, ",time.asctime(time.localtime(st[ST_ATIME])))
            print("Last Modified, ",time.asctime(time.localtime(st[ST_MTIME])))
            print("Last Changed, ", time.asctime(time.localtime(st[ST_CTIME])))
            ##MOREINFO
            if moreinfo == True:        
                print("Extended Stats from os.stat:")
                print("******  ********  ******")
                for item in st:
                    print(item)
                print("******  ********  ******")
            ##THUMBNAILS
            if thumbgo == True:
                print("Converting to Thumbnail")
                nsize = ()
                nsize = (round(img_size[0]/2, 0), round(img_size[1]/2, 0))
                print("New size ", nsize)
                thumbim = im.copy()    
                thumbim.thumbnail(nsize)
                nname = os.path.join(thumbpath, f)
                print(nname)
                thumbim.save(nname)
                thumbim.close() 
            n = os.path.join(targetdirofcopies, f)
            print("new image location is: ")
            print(n)
            im.save(n)
            cents = "*******Image number: " + str(i) + " " + f + " COMPLETE!*********"
            print(cents.center(75))
            print("")
            i += 1
            im.close()
    ###END OF LOOP           
    print(i, " images copied!")
    print("*****batch_makr complete*****")
    print("Navigate to ", targetdirofcopies, " to check results!")
    os.chdir(targetdirofcopies)
    print("Listing files in target directory")
    for f in os.listdir():
        print(f)
    os.chdir(startingplace)
    

batch_makr(whereimagesat, whereimagesgo, "all")
#test_image = os.path.normpath(r'C:\Users\Chris\Pictures\Apollo-11-print.jpg', "all")
#CF_single_image(test_image, defaultdir)



