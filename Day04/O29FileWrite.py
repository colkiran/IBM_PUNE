"""
w = write
you can write data into the file
if file exists then opens the file deletes the content of the file, starts writing into the file

"""


FW = open("myfile.txt", "w")

# st = input("Enter the content of the file :")
# FW.write(st)

l1 = "This is the first line\n"
l2 = "This is the second line\n"
l3 = "This is the third line\n"

FW.writelines([l1,l2,l3])
FW.close()
