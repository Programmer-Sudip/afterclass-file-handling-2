# open the file using the with() function and write breif introduction in the file
with open("Sample_File.txt", "w") as f:
    f.write("Hi, I am Sudip. I am learning Python")
# close the file
f.close()


# open a file and split it into words
with open("Sample_File.txt", "r") as file:
    data = file.readlines()
    for line in data:
        words = line.split()
        print(words)
# close the file
file.close()


#check whether a file names My_File exists or not
import os
if os.path.exists("My_File"):
    print("File exists")
else:
    print("File does not exist")


# Create a file if it is not exists and write content in it
file = open("My_File", "w")
file.write("Hello World !!!")
file.close()





# delete the file
import os
os.remove("Sample_File.txt")