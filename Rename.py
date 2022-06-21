#import this module, need functions from it's library

import os

# define a variable 'path' ensure the files are in this folder the path point to

path = os.chdir("home/airbuff/gif")

#declare a counter variable and give it a value of 0 to ensure the script starts with the first file

x = 0

#write a loop which goes through the files and changes the names

for file in os.listdir(path)

# name the files to what you want them to be

     photos = "geth{}.jpg".format(x)

# using os rename function requires the variables to be passed as parameter 
   
     os.rename(file, photos)


#increment the counter

    x = x + 1

 
