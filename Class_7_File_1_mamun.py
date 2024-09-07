
import os 
os.system('cls')
print()



# overwrite a file 
#f = open("G:\\test2.txt", "w")
# f.write("Woops! I have deleted the content!")
#f.close() 
f = open("G:\\test2.txt", "r")
print("203 : " , f.read(),"\n")
f.close()


# Append data of an Existing file 
f = open("G:\\test2.txt", "a")
f.write("Append,  Now the file has more content!\n")
f.close()

f = open("G:\\test2.txt", "r")

print("204 : " , f.read())

f.seek(0)

print("205 : \n" )


for x in f:
  #for y in x: 
   print("Word :", x) 



f.close()




#open and read the file after the overwriting:
#f = open("demofile3.txt", "r")
#print(f.read())


# f.seek(0)   	 Move file pointer to the beginning of a File
# f.seek(5)	     Move file pointer five characters ahead from the beginning of a file.
# f.seek(0, 2)	 Move file pointer to the end of a File
# f.seek(5, 1)	 Move file pointer five characters ahead from the current position.
# f.seek(-5, 1)	 Move file pointer five characters behind from the current position.
# f.seek(-5, 2)	 Move file pointer in the reverse direction. Move it to the 5th character from the end of the file