
file_1 = 'rtr.txt'
file = open(file_1, mode='r')
file_cont = file.read()
file.close()
print(file_cont)