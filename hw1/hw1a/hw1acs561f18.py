try:
	file = open("input.txt", "r")
	f = open("output.txt", "w")
	for line in file:
		line = line.strip('\n')
		input = line.split(",")
		if input[1] == 'Dirty':
			f.write("Suck\n")
		elif input[0] == 'A':
			f.write("Right\n")
		elif input[0] == 'B':
			f.write("Left\n")
except IOError as err:  
    print('File Error:'+str(err))
 
finally:
    if 'file' in locals():
        file.close()
	

