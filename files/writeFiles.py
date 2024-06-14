new_file_name = 'Example2.txt'
# with open(new_file_name, 'w') as new_file:
#     new_file.write('Hello Im Your Atm')

# lines = ['CHELSEA \n', 'MAN U \n', 'MAN CITY \n', 'BITCHES ARSENAL \n']
# with open(new_file_name, 'a') as testCreatedFile:
#     for line in lines:
#         testCreatedFile.write(line)
#
# with open(new_file_name, 'r') as test:
#     content = test.read()

# copy an existing file into another one

with open('Example2.txt', 'r') as existingFile:
    with open('CopiedFile.txt', 'w') as copiedFile:
        for line in existingFile:
            copiedFile.write(line)
