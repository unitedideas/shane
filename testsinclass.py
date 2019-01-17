print('shane', sep=' ', end='\n', file=None)

file = open('teststyles.css', mode='r', buffering=True, encoding=None, errors=None, newline=None, closefd=True)


for line in file:
    print(line)
    for char in line:
        if char == "\n":
            char = "\\n"
        if char == " ":
            char = "_"
        print(char)
