f=open('myfile.txt', 'r')
while True:
    line=f.readline()
    if not line:
        print(line, type(line))
        break
    print(line)