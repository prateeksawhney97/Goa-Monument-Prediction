import os
# Function to rename multiple files

i = 16
path="images/new/"
for filename in os.listdir(path):
    my_dest ="f_" + str(i) + ".jpeg"
    my_source =path + filename
    my_dest =path + my_dest
    # rename() function will
      # rename all the files
    os.rename(my_source, my_dest)
    i += 1

