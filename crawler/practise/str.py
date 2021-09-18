# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#
stri = []
for i in range(0,10):
    stri.append(i)
    print(stri[i])

stri[5] = "a"
new = ""
for i in range(0,len(stri)):
    if i != len(stri)-1:
        new = new+str(stri[i])+", "
    else:
        new = new+str(stri[i])

print (new)
newstr =[]
newstr.append(new)
print (newstr[0])
