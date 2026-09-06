#write file 

file=open("D:/Full stack/python basic/Day12/newfile.txt","w")
file.write("hello")
file.close()


#read file 
fileread=open("D:/Full stack/python basic/Day12/newfile.txt","r")
print(fileread.read())