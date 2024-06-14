

# basic way

# file = open('Example1.txt','r')
# content = file.read()
# file.close()
#
# print(file.closed)

#using with (more sofisticated)

with open('Example1.txt', 'r') as file:
    # content1 = file.read(10)
    # content2 = file.read(10)
    # content3 = file.read(10)

    content1 = file.readline()
    content = file.read(5)

print(content1)
print(content)



