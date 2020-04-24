# from the python mega course
# to run the entire code remove first ''' pair from code
# create text file named test.txt containg multiple lines

# file handling opening t& reading the file
'''
file = open("test.txt", "r")

content = file.readlines()
# file.read() for all content reading
# file.seek(0) to readjustng the reading pointer
print(content)

content = [i.rstrip('\n') for i in content]
# to remove \n from numbers
print(content)

file.close()
'''


# creating new file or rewrite existing one
'''
file = open('test1.txt', 'w')

file.write("line 1\n")
file.write("line 2\n")

file.close()
'''

# appending existing files
'''
file = open('test1.txt', 'a')

file.write("line 3\n")
file.write("line 4\n")

file.close()
'''

# notes
# r+  =>  both reading and writing , add at beginning of text
# w+  =>  writing and reading , create if it don't exist i.e. it overwrites
# a+  => add at the end


# with method no need to close
'''
with open('test1.txt', 'a+') as file:
    file.seek(0) # to bring pointer at start
    content = file.read()
    file.write("line 5\n")
    file.write("line 6\n")

print(content)
'''

